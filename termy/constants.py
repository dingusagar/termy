import os
from pathlib import Path
from colorama import Fore, Back
import art

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

VERSION = '0.0.6'

MATCH_THRESHOLD = 60

TERMY_CONFIGURE_MESSAGE = Fore.RED + "Termy is not yet configured \n" + Fore.YELLOW + \
                          "Please configure it using " + Fore.GREEN + "termy --configure"
SERVER_ERROR = Fore.RED + "Unable to find the server at sheets.googleapis.com. Please check your connection!"
HTPP_SHEET_ERROR = Fore.RED + "Sheet could not be parsed. Please check if Sheet ID and Sheet Name is correct"
TERMY_BANNER = art.text2art("Termy")
TERMY_INTRO_MESSAGE = Fore.LIGHTYELLOW_EX + f'''
{TERMY_BANNER}
Termy is a terminal assistant which is focussed on easing out the developers life
by triggering commands just based on the Natural language.

To get started:
Configure termy using ''' + Fore.LIGHTGREEN_EX + '''termy --configure .''' + Fore.LIGHTYELLOW_EX + '''This will connect termy to your google sheet containg commands.
Once configuration is done, you can search using''' + Fore.LIGHTGREEN_EX + ''' termy <search_text> ''' + \
                      Fore.LIGHTYELLOW_EX + '''\nYou can also visit https://pypi.org/project/termy/ for more details \n\nIf you have any feedbacks on this tool, please use this form : https://forms.gle/8sHNPD9PNyVupFht8
You can also visit our github page and raise issues there. : https://github.com/dingusagar/termy
'''
AUTHENTICATE_ERROR = "Failed to authenticate google sheets integration"

SHEET_ID_INPUT_MESSAGE = f'''{Fore.LIGHTCYAN_EX}
Termy needs the sheet id of your google sheet link.

How to find your sheet id ?
Sheet id for the following sample sheet is the highlighted part : https://docs.google.com/spreadsheets/d/{Back.WHITE}{Fore.BLACK}1-wtkODsgt0EJzARAo7BBNOXwkd1W3vDiPH1HZoyskXI{Back.RESET}{Fore.LIGHTCYAN_EX}/edit#gid=0  

Enter the Sheet ID for your google sheet : {Fore.RESET}'''

SHEET_LINK_INPUT = f'''{Fore.LIGHTCYAN_EX}
Termy needs the google sheet link where the commands and queries are stored.

Your google sheet should follow the same format as this sample sheet : https://docs.google.com/spreadsheets/d/1-wtkODsgt0EJzARAo7BBNOXwkd1W3vDiPH1HZoyskXI/edit#gid=0  

Paste your google sheet link here : {Fore.RESET}'''

INVALID_SHEET_LINK = f'''{Fore.RED}Invalid Sheet Link.
Google sheet link should look something like this : https://docs.google.com/spreadsheets/d/1-wtkODsgt0EJzARAo7BBNOXwkd1W3vDiPH1HZoyskXI/edit#gid=0
Try again with the proper sheet link. {Fore.RESET}'''
