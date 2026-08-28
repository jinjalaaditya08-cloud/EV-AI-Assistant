"""
Context manager (Phase 1)
Stores short-term context in-memory. Long-term context will use MemoryManager.
"""

class ContextManager:
    def __init__(self):
        self._context = {
            'session_id': None,
            'recent_messages': [],
        }

    def push_message(self, role, text):
        self._context['recent_messages'].append({'role': role, 'text': text})
        # keep last 20
        self._context['recent_messages'] = self._context['recent_messages'][-20:]

    def get_context(self):
        return self._context

    def clear(self):
        self._context = {'session_id': None, 'recent_messages': []}
