# Basic buildozer.spec for Kivy app (Phase 1)

[app]
title = E.V. - Eternal Voice (Phase1)
package.name = ev
package.domain = org.everlasting
source.dir = .

# requirements - keep minimal for Phase 1
requirements = python3,kivy,kivymd

# Android settings
android.api = 31
android.minapi = 30
android.permissions = INTERNET


[buildozer]
log_level = 2
