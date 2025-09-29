[app]
# Название приложения (отображается на телефоне)
title = Video Downloader

# Уникальное имя пакета (можно изменить)
package.name = videodownloader
package.domain = org.example

# Папка с исходным кодом
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Версия
version = 1.0

# Что нужно для работы
requirements = python3,kivy,yt-dlp,requests,setuptools,wheel

# Экран только вертикальный
orientation = portrait

# Полноэкранный режим (0 = нет)
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
