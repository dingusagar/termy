import json
import os.path

from colorama import Fore
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from termy.constants import TOKEN_JSON, SCOPES, AUTHENTICATE_ERROR
from termy.exception.custom_exceptions import GoogleSheetAuthRequiredException, GoogleSheetNotFoundException, \
    UnknownException
from termy.utils.utils import log_s5864, apply_color_and_rest, log_keydev


def google_auth_renew():
    try:
        os.remove(TOKEN_JSON) if os.path.exists(TOKEN_JSON) else None
        flow = InstalledAppFlow.from_client_config(
            log_s5864(), SCOPES)
        creds = flow.run_local_server(port=0)
        with open(TOKEN_JSON, 'w') as token:
            token.write(creds.to_json())
        return creds
    except Exception as e:
        print(apply_color_and_rest(Fore.RED, AUTHENTICATE_ERROR), e)


def connect_to_google_sheet(sheet_id, credentials=None):
    try:
        service = build('sheets', 'v4', credentials=credentials, developerKey=log_keydev())
        sheet_client = service.spreadsheets()
        sheet_metadata = service.spreadsheets().get(spreadsheetId=sheet_id).execute()
        return sheet_client, sheet_metadata
    except HttpError as err:
        err_response = json.loads(err.content)
        error_status = err_response.get('error').get('status')
        if error_status == 'PERMISSION_DENIED':
            raise GoogleSheetAuthRequiredException
        elif error_status == 'NOT_FOUND':
            raise GoogleSheetNotFoundException
        else:
            raise UnknownException(err)
