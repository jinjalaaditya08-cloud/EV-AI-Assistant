"""
Core application bootstrap for E.V. — Phase 1
Initializes configuration, logger, database and basic services.
"""

from kivy.app import App
from kivy.uix.label import Label

from config import AppConfig
from utils.logger import get_logger
from database.database import Database

LOGGER = get_logger('EVApp')

class EVApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config = AppConfig()
        self.db = Database(self.config.database_path)
        self.logger = LOGGER

    def build(self):
        self.logger.info('E.V. App starting (Phase 1)')
        # Placeholder simple UI for Phase 1
        return Label(text='E.V. — Eternal Voice\nPhase 1: Core Initialized')

