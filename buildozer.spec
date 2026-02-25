[app]
title = AP Test
package.name = aptest
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg,ttf,atlas
version = 0.1.0
orientation = portrait
fullscreen = 0
requirements = python3,kivy,kivymd,requests,beautifulsoup4
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.archs = armeabi-v7a, arm64-v8a, x86, x86_64
android.minapi = 21
android.allow_cleartext_traffic = 1
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 0
bin_dir = bin
build_dir = .buildozer

[app_android]
android.gradle_dependencies =
android.manifest.placeholders =

[app_android:debug]

[app_android:release]

[app:source.exclude_patterns]
*.pyc, __pycache__/, .git/, .github/
