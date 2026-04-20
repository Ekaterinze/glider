[app]
title = Planer
package.name = planer
package.domain = org.wiseplat
source.dir = .
version = 0.1

# 🔥 Исправлено: без пробелов перед запятой
requirements = python3,kivy==2.2.1,kivymd==1.1.1

presplash.filename = %(source.dir)s/data/logo/presplash512okmin.png
icon.filename = %(source.dir)s/data/logo/logo512min.png

# Ориентация: закомментировано = авто-поворот (по умолчанию)
orientation = portrait

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