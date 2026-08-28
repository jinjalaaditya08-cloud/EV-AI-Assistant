"""
Simple intent engine (Phase 1)
Uses rule-based fallback intent classification. Replace with ML models in Phase 2.
"""

class IntentEngine:
    def __init__(self):
        # In Phase 1, a tiny set of intents for demonstration.
        self.intents = ['chat', 'research', 'code', 'camera', 'memory', 'unknown']

    def classify(self, text: str) -> str:
        t = (text or '').lower()
        if any(w in t for w in ['research', 'search', 'look up']):
            return 'research'
        if any(w in t for w in ['code', 'fix', 'generate']):
            return 'code'
        if any(w in t for w in ['camera', 'photo', 'image', 'what is']):
            return 'camera'
        if any(w in t for w in ['remember', 'forget', 'memory']):
            return 'memory'
        if any(w in t for w in ['hi', 'hello', 'hey', 'how are you']):
            return 'chat'
        return 'unknown'
