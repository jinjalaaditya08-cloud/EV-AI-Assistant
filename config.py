"""
Central configuration for E.V.
Keep secrets out of source -- load via environment variables or external config in later phases.
"""

import os
from pathlib import Path

ROOT_DIR = Path(__file__).parent

class AppConfig:
    APP_NAME = 'E.V. — Eternal Voice'
    APP_VERSION = '0.1.0'

    # Database path (inside app storage) - can be overridden by environment variable
    database_path = os.environ.get('EV_DATABASE_PATH', str(ROOT_DIR / 'ev_data' / 'ev_database.sqlite3'))

    # AI provider settings (abstract) - set via environment in later phases
    AI_PROVIDER = os.environ.get('EV_AI_PROVIDER', 'local')
    AI_API_KEY = os.environ.get('EV_API_KEY', '')

    # Runtime options
    DEBUG = os.environ.get('EV_DEBUG', '1') == '1'
    MAX_CODE_RETRIES = int(os.environ.get('EV_MAX_CODE_RETRIES', '5'))

