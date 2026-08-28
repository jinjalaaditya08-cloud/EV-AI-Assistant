E.V. — Eternal Voice (Phase 1)

This repository contains the Phase 1 implementation for E.V. — a modular mobile-first AI assistant.

Phase 1 Objective
- Create the core architecture, configuration system, database schema and minimal app bootstrap.

What I added in Phase 1
- App bootstrap (main.py, app.py)
- Central configuration and constants
- Core AI brain stubs (ai_brain, intent engine, context manager)
- SQLite database wrapper with migrations
- History and memory database helpers
- Memory manager API
- Structured logger
- buildozer.spec (minimal)

How to run (development)
- Install Python 3.10+ and Kivy/KivyMD per their docs.
- From project root run: python main.py

NOTE: Android platform integrations (camera, microphone, services) are not implemented in Phase 1 and are marked as PLATFORM IMPLEMENTATION REQUIRED.

Next steps (Phase 2)
- Implement AI provider abstraction
- Replace rule-based intent engine with model-backed intent classifier
- Add provider connectors (OpenAI/Anthropic/local)
- Create initial UI screens (home/chat)

