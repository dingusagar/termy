import os.path

from colorama import Fore
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from termy.constants import TOKEN_JSON, SCOPES, AUTHENTICATE_ERROR
from termy.utils.utils import log_s5864, apply_color_and_rest


def google_auth():
    try:
        creds = None
        # os.remove(TOKEN_JSON)
        if os.path.exists(TOKEN_JSON):
            creds = Credentials.from_authorized_user_file(TOKEN_JSON, SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_config(
                    log_s5864(), SCOPES)
                creds = flow.run_local_server(port=0)
            with open(TOKEN_JSON, 'w') as token:
                token.write(creds.to_json())

        return creds
    except Exception as e:
        print(apply_color_and_rest(Fore.RED, AUTHENTICATE_ERROR), e)

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

