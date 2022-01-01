import csv
import os.path

from colorama import Fore
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from httplib2 import ServerNotFoundError
from tqdm import tqdm

from termy.constants import TERMY_COMMANDS_FILE, SERVER_ERROR, HTPP_SHEET_ERROR
from termy.utils import apply_color_and_rest


def get_sheet_content_into_csv(SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, creds):
    try:
        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print(apply_color_and_rest(Fore.RED, 'No data found :('))
            return

        if os.path.exists(TERMY_COMMANDS_FILE) and os.path.isfile(TERMY_COMMANDS_FILE):
            os.remove(TERMY_COMMANDS_FILE)
        file_with_commands = open(TERMY_COMMANDS_FILE, 'w')
        writer = csv.writer(file_with_commands)
        for row in tqdm(values, desc="Updating Data ", colour='#32CD32'):
            writer.writerow(row)
        file_with_commands.close()
        print(apply_color_and_rest(Fore.LIGHTCYAN_EX, f'Saved data at {TERMY_COMMANDS_FILE}'))
    except ServerNotFoundError as err:
        print(SERVER_ERROR)
    except HttpError as err:
        print(HTPP_SHEET_ERROR)
