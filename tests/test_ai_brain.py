"""
Unit tests for ai_brain integration with a local provider (Phase 2)
"""

from database.database import Database
from memory.memory_database import MemoryDatabase
from memory.memory_manager import MemoryManager
from ai_provider.local_provider import LocalProvider
from core.ai_brain import AIBrain
import tempfile

def test_ai_brain_handle_text_tmp_db(tmp_path):
    db_path = str(tmp_path / 'testdb.sqlite3')
    db = Database(db_path)
    mem_db = MemoryDatabase(db)
    mem_mgr = MemoryManager(mem_db)
    provider = LocalProvider()
    brain = AIBrain(memory_manager=mem_mgr, ai_provider=provider)

    out = brain.handle_text('Hello, how are you?')
    assert out['status'] == 'ok'
    assert 'response' in out
    assert out['intent'] in ['chat', 'unknown']
