"""
Updated app bootstrap to wire the LocalProvider into the AIBrain (Phase 2)
"""

from kivy.app import App
from kivy.uix.label import Label

from config import AppConfig
from utils.logger import get_logger
from database.database import Database

# Phase 2 imports
from ai_provider.local_provider import LocalProvider
from memory.memory_database import MemoryDatabase
from memory.memory_manager import MemoryManager
from core.ai_brain import AIBrain

LOGGER = get_logger('EVApp')

class EVApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config = AppConfig()
        self.db = Database(self.config.database_path)
        self.logger = LOGGER

        # Phase 2: initialize memory manager and local AI provider
        self.mem_db = MemoryDatabase(self.db)
        self.memory_manager = MemoryManager(self.mem_db)
        self.ai_provider = LocalProvider(config={'provider': 'local'})
        self.brain = AIBrain(memory_manager=self.memory_manager, ai_provider=self.ai_provider)

    def build(self):
        self.logger.info('E.V. App starting (Phase 2) - AI provider wired')
        # Placeholder simple UI for Phase 2 (UI screens to come in Phase 2 continuation)
        return Label(text='E.V. — Eternal Voice\nPhase 2: AI Provider Wired')
