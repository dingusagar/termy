import os
from pathlib import Path
from colorama import Fore, Back
import art

APP_NAME = 'termy'
TERMY_DIR = Path.home() / APP_NAME
TERMY_COMMANDS_FILE = TERMY_DIR / 'commands.csv'
CONFIG = TERMY_DIR / 'config.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
app_root = os.path.dirname(__file__)
CREDENTIALS_JSON = os.path.join(app_root, 'resources/credentials.json')
TOKEN_JSON = os.path.join(app_root, 'resources/tokens.json')
CREDS_OBJECT_FILE = os.path.join(app_root, "resources/creds.pkl")
GPT3_CONFIG = os.path.join(app_root, "resources/gpt3_config.json")
SHEET_NAME = "Sheet1"
GITHUB_ISSUES_URL = "https://github.com/dingusagar/termy/issues"

VERSION = '0.0.17'

class ConfigKeys:
    LAST_UPDATED_AT = 'last_updated_at'
    CHECK_UPDATE_AFTER = 'check_for_update_after(days)'
    AUTH_REQUIRED = 'auth_required'
    SHEET_ID = 'sheet_id'
    SHEET_LINK = 'sheet_link'

class ColNames:
    QUERY = 'queries'
    COMMANDS = 'commands'


SAMPLE_SHEET_LINK = 'https://docs.google.com/spreadsheets/d/1-wtkODsgt0EJzARAo7BBNOXwkd1W3vDiPH1HZoyskXI/edit#gid=0'

MATCH_THRESHOLD = 60

TERMY_CONFIGURE_MESSAGE = Fore.RED + "Termy is not yet configured \n" + Fore.YELLOW + \
                          "Please configure it using " + Fore.GREEN + "termy --configure"
SERVER_ERROR = Fore.RED + "Unable to find the server at sheets.googleapis.com. Please check your connection!"
HTPP_SHEET_ERROR = Fore.RED + "Sheet could not be parsed. Please check if Sheet ID and Sheet Name is correct"

AUTHENTICATION_FAILED_ON_UPDATE_ERROR = f'''{Fore.RED}
Failed to authenticate to your google sheet for updating data. 
Make sure you are trying to login with the account that has access to the google sheet. 
Try {Fore.GREEN} termy --configure {Fore.RED} again 
{Fore.RESET}
'''

SHEET_NOT_FOUND_ERROR = f'''{Fore.RED}
Could not find the google sheet. Please recheck the sheet url you gave.
Try {Fore.GREEN} termy --configure {Fore.RED} again 
{Fore.RESET}
'''

UNKNOWN_EXCEPTION_ERROR = f'''{Fore.RED}
Oops..Something went wrong. Try {Fore.GREEN} termy --configure {Fore.RED} again.
If it does't help please raise an issue here {GITHUB_ISSUES_URL} with the details of the error message. We will get back to you.
{Fore.RESET}
'''

TERMY_BANNER = art.text2art("Termy")
TERMY_INTRO_MESSAGE = Fore.LIGHTYELLOW_EX + f'''
{TERMY_BANNER}
Termy is a terminal assistant which is focussed on easing out the developers life
by triggering commands just based on the Natural language.

To get started:
Configure termy using ''' + Fore.LIGHTGREEN_EX + '''termy --configure .''' + Fore.LIGHTYELLOW_EX + '''This will connect termy to your google sheet containg commands.
Once configuration is done, you can search using''' + Fore.LIGHTGREEN_EX + ''' termy <search_text> ''' + \
                      Fore.LIGHTYELLOW_EX + '''\n\n\nYou can also visit https://pypi.org/project/termy/ for more details \n\nIf you have any feedbacks on this tool, please use this form : https://forms.gle/8sHNPD9PNyVupFht8
You can also visit our github page and raise issues there. : https://github.com/dingusagar/termy
'''
AUTHENTICATE_ERROR = "Failed to authenticate google sheets integration"

SHEET_LINK_INPUT = f'''{Fore.LIGHTCYAN_EX}
Termy needs the google sheet link where the commands and queries are stored.

Your google sheet should follow the same format as this sample sheet : {SAMPLE_SHEET_LINK} 

Paste your google sheet link here : {Fore.RESET}'''

INVALID_SHEET_LINK = f'''{Fore.RED}Invalid Sheet Link.
Google sheet link should look something like this : {SAMPLE_SHEET_LINK}
Try again with the proper sheet link. {Fore.RESET}'''

EMPTY_SHEET_MESSAGE = f'''{Fore.RED}Did not find valid data in the sheet.
Please refer to the sample sheet and add contents to your sheet in the same format
Sample sheet : {SAMPLE_SHEET_LINK} {Fore.RESET}
'''

GPT3_API_KEY_INPUT = f'''{Fore.LIGHTCYAN_EX}
Need API Key for querying to GPT-3. If you dont have one, sign up for an account and get it by clicking the link here https://beta.openai.com/account/api-keys 

API KEY :{Fore.RESET} '''


GOOGLE_AUTH_PROMPT_ON_UNAUTHORISED_SHEET = f'''{Fore.LIGHTCYAN_EX}
The google sheet you provided does not have public read access.
You can either modify the sharing permission on the sheet by selecting 'Anyone with the link' option and giving view access.
Or you can authenticate termy with your google account to access the sheet. 

Proceed with Google Authentication (y/n) : 
{Fore.RESET}'''

STOPWORDS = {'plz', 'pls', 'want', 'can', 'you', 'get', 'check', 'the', 'a', 'able', 'about', 'above', 'abst',
             'accordance', 'according', 'accordingly', 'across', 'act', 'actually', 'added', 'adj', 'affected',
             'affecting', 'affects', 'after', 'afterwards', 'again', 'against', 'ah', 'all', 'almost', 'alone', 'along',
             'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'announce', 'another',
             'any', 'anybody', 'anyhow', 'anymore', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apparently',
             'approximately', 'are', 'aren', 'arent', 'arise', 'around', 'as', 'aside', 'ask', 'asking', 'at', 'auth',
             'available', 'away', 'awfully', 'b', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming',
             'been', 'before', 'beforehand', 'begin', 'beginning', 'beginnings', 'begins', 'behind', 'being', 'believe',
             'below', 'beside', 'besides', 'between', 'beyond', 'biol', 'both', 'brief', 'briefly', 'but', 'by', 'c',
             'ca', 'came', 'can', 'cannot', "can't", 'cause', 'causes', 'certain', 'certainly', 'co', 'com', 'come',
             'comes', 'contain', 'containing', 'contains', 'could', 'couldnt', 'd', 'date', 'did', "didn't",
             'different', 'do', 'does', "doesn't", 'doing', 'done', "don't", 'down', 'downwards', 'due', 'during', 'e',
             'each', 'ed', 'edu', 'effect', 'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ending',
             'enough', 'especially', 'et', 'et-al', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone',
             'everything', 'everywhere', 'ex', 'except', 'f', 'far', 'few', 'ff', 'fifth', 'first', 'five', 'fix',
             'followed', 'following', 'follows', 'for', 'former', 'formerly', 'forth', 'found', 'four', 'from',
             'further', 'furthermore', 'g', 'gave', 'get', 'gets', 'getting', 'give', 'given', 'gives', 'giving', 'go',
             'goes', 'gone', 'got', 'gotten', 'h', 'had', 'happens', 'hardly', 'has', "hasn't", 'have', "haven't",
             'having', 'he', 'hed', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'heres', 'hereupon',
             'hers', 'herself', 'hes', 'hi', 'hid', 'him', 'himself', 'his', 'hither', 'home', 'how', 'howbeit',
             'however', 'hundred', 'i', 'id', 'ie', 'if', "i'll", 'im', 'immediate', 'immediately', 'importance',
             'important', 'in', 'inc', 'indeed', 'index', 'information', 'instead', 'into', 'invention', 'inward', 'is',
             "isn't", 'it', 'itd', "it'll", 'its', 'itself', "i've", 'j', 'just', 'k', 'keep', 'keeps', 'kept', 'kg',
             'km', 'know', 'known', 'knows', 'l', 'largely', 'last', 'lately', 'later', 'latter', 'latterly', 'least',
             'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'line', 'little', "'ll", 'look', 'looking',
             'looks', 'ltd', 'm', 'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'me', 'mean', 'means',
             'meantime', 'meanwhile', 'merely', 'mg', 'might', 'million', 'miss', 'ml', 'more', 'moreover', 'most',
             'mostly', 'mr', 'mrs', 'much', 'mug', 'must', 'my', 'myself', 'n', 'na', 'name', 'namely', 'nay', 'nd',
             'near', 'nearly', 'necessarily', 'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'new',
             'next', 'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'nor', 'normally', 'nos',
             'not', 'noted', 'nothing', 'now', 'nowhere', 'o', 'obtain', 'obtained', 'obviously', 'of', 'off', 'often',
             'oh', 'ok', 'okay', 'old', 'omitted', 'on', 'once', 'one', 'ones', 'only', 'onto', 'or', 'ord', 'other',
             'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'owing',
             'own', 'p', 'page', 'pages', 'part', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed',
             'please', 'plus', 'poorly', 'possible', 'possibly', 'potentially', 'pp', 'predominantly', 'present',
             'previously', 'primarily', 'probably', 'promptly', 'proud', 'provides', 'put', 'q', 'que', 'quickly',
             'quite', 'qv', 'r', 'ran', 'rather', 'rd', 're', 'readily', 'really', 'recent', 'recently', 'ref', 'refs',
             'regarding', 'regardless', 'regards', 'related', 'relatively', 'research', 'respectively', 'resulted',
             'resulting', 'results', 'right', 'run', 's', 'said', 'same', 'saw', 'say', 'saying', 'says', 'sec',
             'section', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sent',
             'seven', 'several', 'shall', 'she', 'shed', "she'll", 'shes', 'should', "shouldn't", 'show', 'showed',
             'shown', 'showns', 'shows', 'significant', 'significantly', 'similar', 'similarly', 'since', 'six',
             'slightly', 'so', 'some', 'somebody', 'somehow', 'someone', 'somethan', 'something', 'sometime',
             'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specifically', 'specified', 'specify',
             'specifying', 'still', 'stop', 'strongly', 'sub', 'substantially', 'successfully', 'such', 'sufficiently',
             'suggest', 'sup', 'sure'}
