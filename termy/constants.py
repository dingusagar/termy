import os
from pathlib import Path
from colorama import Fore

APP_NAME = 'termy'
TERMY_DIR = Path.home() / APP_NAME
TERMY_COMMANDS_FILE = TERMY_DIR / 'commands.csv'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
app_root = os.path.dirname(__file__)
CREDENTIALS_JSON = os.path.join(app_root, 'resources/credentials.json')
TOKEN_JSON = os.path.join(app_root, 'resources/tokens.json')
CREDS_OBJECT_FILE = os.path.join(app_root, "resources/creds.pkl")
CONFIG = os.path.join(app_root, "resources/config.json")
SHEET_NAME = "Sheet1"

MATCH_THRESHOLD = 60

TERMY_CONFIGURE_MESSAGE = Fore.RED + "Termy is not yet configured \n" + Fore.YELLOW + \
                          "Please configure it using " + Fore.GREEN + "termy --configure"
SERVER_ERROR = Fore.RED + "Unable to find the server at sheets.googleapis.com. Please check your connection!"
HTPP_SHEET_ERROR = Fore.RED + "Sheet could not be parsed. Please check if Sheet ID and Sheet Name is correct"
TERMY_INTRO_MESSAGE = Fore.LIGHTYELLOW_EX + '''
Termy is a terminal assistant which is focussed on easing out the developers life
by triggering commands just based on the Natural language.

To get started:
Configure termy using ''' + Fore.LIGHTGREEN_EX + '''termy --configure .''' + Fore.LIGHTYELLOW_EX + '''This 
will connect termy to your google sheet containg commands.
Once configuration is done, you can search using''' + Fore.LIGHTGREEN_EX + ''' termy <search_text> ''' + \
                      Fore.LIGHTYELLOW_EX + '''\nYou can aslo visit https://pypi.org/project/termy/
                       for more details \n\nIf you have any feedbacks on this tool, please use this form 
                       : https://forms.gle/8sHNPD9PNyVupFht8
You can also visit our github page and raise issues there. : https://github.com/dingusagar/termy
'''
AUTHENTICATE_ERROR = "Failed to authenticate google sheets integration"
