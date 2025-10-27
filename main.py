# 📁 pintelnet_pro/main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import requests
import json

class PintelNetApp(App):
    def __init__(self):
        super().__init__()
        # 👇 CAMBIA ESTA URL POR TU IP REAL
        self.url_base = "http://192.168.0.102:8000"
    
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Título
        title = Label(
            text='[b]📱 PINTELNET[/b]\\nSistema de Instaladores',
            markup=True,
            size_hint_y=0.15,
            font_size='18sp'
        )
        layout.add_widget(title)
        
        # Botones
        btn_scan = Button(
            text='🔍 ESCANEAR DISPOSITIVOS', 
            size_hint_y=0.12,
            background_color=(0.2, 0.6, 1, 1),
            on_press=self.escanear_dispositivos
        )
        layout.add_widget(btn_scan)
        
        btn_clientes = Button(
            text='👤 VER CLIENTES', 
            size_hint_y=0.12,
            background_color=(0.3, 0.8, 0.3, 1),
            on_press=self.ver_clientes
        )
        layout.add_widget(btn_clientes)
        
        # Área de resultados
        self.resultado = Label(
            text='[i]Presiona un botón para comenzar...[/i]',
            markup=True,
            size_hint_y=0.61,
            text_size=(350, None),
            valign='top'
        )
        
        scroll = ScrollView()
        scroll.add_widget(self.resultado)
        layout.add_widget(scroll)
        
        return layout
    
    def escanear_dispositivos(self, instance):
        self.resultado.text = "🔍 Escaneando dispositivos...\\n\\nEspera por favor..."
        
        def hacer_escaneo(dt):
            try:
                response = requests.post(f"{self.url_base}/api/escanear_dispositivos", timeout=15)
                data = response.json()
                
                if data['status'] == 'success':
                    dispositivos = data['dispositivos']
                    texto = f"[b]✅ {len(dispositivos)} DISPOSITIVOS ENCONTRADOS:[/b]\\n\\n"
                    for i, device in enumerate(dispositivos, 1):
                        texto += f"[b]{i}. {device['nombre']}[/b]\\n"
                        texto += f"   Tipo: {device['tipo']}\\n"
                        texto += f"   IP: {device['ip']}\\n\\n"
                    self.resultado.text = texto
                else:
                    self.resultado.text = f"[color=ff3333]❌ Error: {data.get('message', 'Error desconocido')}[/color]\\n\\nRevisa la conexión al servidor."
                    
            except Exception as e:
                self.resultado.text = f"""[color=ff3333]❌ ERROR DE CONEXIÓN[/color]

No se pudo conectar al servidor:
{str(e)}

[color=ffff00]• Verifica que el servidor esté encendido
• Revisa la URL: {self.url_base}
• Asegúrate de estar en la misma red[/color]"""
        
        Clock.schedule_once(hacer_escaneo, 0.1)
    
    def ver_clientes(self, instance):
        self.resultado.text = "📋 Cargando lista de clientes...\\n\\nEspera por favor..."
        
        def cargar_clientes(dt):
            try:
                response = requests.get(f"{self.url_base}/api/clientes", timeout=15)
                data = response.json()
                
                if data['status'] == 'success':
                    clientes = data['clientes']
                    if clientes:
                        texto = f"[b]👥 {len(clientes)} CLIENTES REGISTRADOS:[/b]\\n\\n"
                        for cliente in clientes:
                            texto += f"[b]• {cliente['nombre']}[/b]\\n"
                            texto += f"  📞 {cliente['telefono']}\\n"
                            texto += f"  📍 {cliente['direccion']}\\n"
                            texto += f"  📱 {cliente['dispositivos']} dispositivos\\n\\n"
                    else:
                        texto = "[i]No hay clientes registrados aún.[/i]"
                    self.resultado.text = texto
                else:
                    self.resultado.text = f"[color=ff3333]❌ Error: {data.get('message', 'Error desconocido')}[/color]"
                    
            except Exception as e:
                self.resultado.text = f"[color=ff3333]❌ Error de conexión: {str(e)}[/color]"
        
        Clock.schedule_once(cargar_clientes, 0.1)

if __name__ == '__main__':
    PintelNetApp().run()