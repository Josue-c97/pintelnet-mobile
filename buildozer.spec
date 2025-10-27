# 📁 pintelnet_pro/buildozer.spec
[app]
title = PintelNet Instaladores
package.name = pintelnet
package.domain = org.pintelnet

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt

version = 1.0
requirements = python3,kivy,requests,openssl,android

[buildozer]
log_level = 2

[android]
api = 33
minapi = 21
ndk = 25b
permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE

[android:entrypoint]
main = main:PintelNetApp().run()

[android:meta-data]
android.app.uses_cleartext_traffic = true

[android:activity]
android:usesCleartextTraffic = true