from pathlib import Path

APP_NAME = 'termy'
TERMY_DIR = Path.home() / APP_NAME
# TERMY_DIR = Path('/media/dingusagar/Data/HobbyStuffs/termy/data')
TERMY_COMMANDS_FILE = TERMY_DIR / 'global_commands.csv'

MATCH_THRESHOLD = 80