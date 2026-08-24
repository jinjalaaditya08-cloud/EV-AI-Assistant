import json
import os
from datetime import datetime

class SettingsManager:
    """Manages application settings and user preferences"""
    
    def __init__(self):
        self.settings_file = "ev_settings.json"
        self.default_settings = {
            "dark_mode": True,
            "accent_color": "#00E5FF",
            "font_size": 14,
            "language": "en",
            "notification_sound": True,
            "auto_research": False,
            "theme": "cyberpunk"
        }
        self.settings = self.load_settings()
    
    def load_settings(self):
        """Load settings from file or create default"""
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, 'r') as f:
                    return json.load(f)
            except:
                return self.default_settings.copy()
        return self.default_settings.copy()
    
    def save_settings(self):
        """Save settings to file"""
        with open(self.settings_file, 'w') as f:
            json.dump(self.settings, f, indent=2)
    
    def get(self, key, default=None):
        """Get a setting value"""
        return self.settings.get(key, default)
    
    def set(self, key, value):
        """Set a setting value"""
        self.settings[key] = value
        self.save_settings()
    
    def reset_to_default(self):
        """Reset all settings to default"""
        self.settings = self.default_settings.copy()
        self.save_settings()
    
    def get_all(self):
        """Get all settings"""
        return self.settings.copy()
