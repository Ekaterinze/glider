[app]
title = Glider
package.name = glider
package.domain = org.wiseplat
source.dir = .
version = 0.1

# 🔥 Исправлено: без пробелов перед запятой
requirements = python3,kivy==2.0.0,https://github.com/kivymd/KivyMD/archive/3274d62.zip,sdl2_ttf==2.0.15

presplash.filename = %(source.dir)s/data/logo/presplash512okmin.png
icon.filename = %(source.dir)s/data/logo/logo512min.png

# Ориентация: закомментировано = авто-поворот (по умолчанию)
#orientation = sensor

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
# 🔥 Обновите API до актуального
android.api = 33
android.minapi = 21

# 🔥 Архитектуры: 32 + 64 бит
android.archs = arm64-v8a

# 🔥 Критично для CI/CD
android.accept_sdk_license = True

# 🔥 Рекомендуется для совместимости
android.enable_androidx = True

# 🔥 Разрешения (если нужно)
android.permissions = INTERNET,ACCESS_NETWORK_STATE