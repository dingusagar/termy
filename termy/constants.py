import os
from pathlib import Path

APP_NAME = 'termy'
TERMY_DIR = Path.home() / APP_NAME
# TERMY_DIR = Path('/media/dingusagar/Data/HobbyStuffs/termy/data')
TERMY_COMMANDS_FILE = TERMY_DIR / 'commands.csv'

MATCH_THRESHOLD = 80

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
app_root = os.path.dirname(__file__)
CREDENTIALS_JSON = os.path.join(app_root, 'resources/credentials.json')

TOKEN_JSON = os.path.join(app_root, 'resources/tokens.json')
CREDS_OBJECT_FILE = os.path.join(app_root, "resources/creds.pkl")
CONFIG = os.path.join(app_root, "resources/config.json")
SHEET_NAME = "Sheet1"
