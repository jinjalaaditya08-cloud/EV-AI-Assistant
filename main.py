"""
E.V. — Eternal Voice
Entry point for the Kivy application (Phase 1).

This file keeps the launcher minimal. The real app lives in app.py.
"""

from kivy import Config
# Minimal Kivy configuration for mobile friendliness
Config.set('kivy', 'keyboard_mode', 'systemanddock')

from app import EVApp

if __name__ == '__main__':
    EVApp().run()
