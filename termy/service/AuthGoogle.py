import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from termy.service import Constants
from termy.service.get_sheet_content import get_sheet_content_into_csv


def google_auth():
    creds = None
    if os.path.exists(Constants.TOKEN_JSON):
        creds = Credentials.from_authorized_user_file(Constants.TOKEN_JSON, Constants.SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                Constants.CREDENTIALS_JSON, Constants.SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(Constants.TOKEN_JSON, 'w') as token:
            token.write(creds.to_json())

    return creds

creds = google_auth()
get_sheet_content_into_csv('17wxgSK32mOd96Z8R_93DnosGiJXJkCDicitMaaF2ArE', 'Sheet1', creds)