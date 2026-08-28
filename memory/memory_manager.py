"""
Memory manager (Phase 1)
Provides a controlled API for storing and retrieving memory.
Later phases will add validation, importance scoring and privacy controls.
"""

from memory.memory_database import MemoryDatabase

class MemoryManager:
    def __init__(self, mem_db: MemoryDatabase):
        self.db = mem_db

    def remember(self, key: str, value: str, category: str = 'general'):
        return self.db.store(key, value, category)

    def recall(self, key: str):
        return self.db.retrieve(key)

    def list_memory(self):
        return self.db.list_all()
