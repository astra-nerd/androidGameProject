[app]
title = My Kivy Game
package.name = androidgameproject
package.domain = org.testgame
source.dir = .
source.include_exts = py,png
version = 0.1
requirements = python3,kivy==2.3.1
orientation = landscape
fullscreen = 1
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
