[app]
title = PintelNet Mobile
package.name = pintelnet
package.domain = org.pintelnet

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy,requests

[buildozer]
log_level = 2

[android]
# Skip license check
android.accept_sdk_license = True

# Android configuration
api = 34
minapi = 21
ndk_api = 21

# Permissions
android.permissions = INTERNET

# Architectures  
android.arch = arm64-v8a, armeabi-v7a
