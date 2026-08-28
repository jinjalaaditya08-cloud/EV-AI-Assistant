E.V. — Eternal Voice (Phase 2)

Phase 2 Objective
- Implement AIProvider abstraction and a LocalProvider stub.
- Wire the LocalProvider into the AIBrain and EVApp bootstrap so the app uses the provider for intent classification and response generation.

What I changed / added
- ai_provider package with base interface and local implementation
- AIBrain updated to use AIProvider for classify/generate with fallbacks
- app.py updated to initialize MemoryManager and LocalProvider and pass them into AIBrain
- Basic pytest unit tests for the provider and ai_brain

How to run tests
- Install pytest
- Run: pytest tests/test_ai_provider.py tests/test_ai_brain.py

Next steps (Phase 2 continuation)
- Implement the home and chat UI screens and wire them to the EVApp
- Add AIProvider adapters for OpenAI / Anthropic (optional plugins behind config)
- Replace rule-based intent engine with a model-backed classifier (via provider) when available
