import csv
import os.path

from colorama import Fore
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from httplib2 import ServerNotFoundError
from tqdm import tqdm

from termy.constants import TERMY_COMMANDS_FILE, SERVER_ERROR, HTPP_SHEET_ERROR, ColNames
from termy.utils import apply_color_and_rest


def is_valid_format(values):
    if not values:
        return False

    header = values[0]
    if ColNames.QUERY in header and ColNames.COMMANDS in header:
        return True

    return False


def get_sheet_content_into_csv(sheet_id, creds):
    try:
        service = build('sheets', 'v4', credentials=creds)

        sheet_client = service.spreadsheets()
        sheet_metadata = service.spreadsheets().get(spreadsheetId=sheet_id).execute()
        sheets = sheet_metadata.get('sheets', '')
        sheet_names = [sheet['properties']['title'] for sheet in sheets]

        if not sheet_names:
            print(apply_color_and_rest(Fore.RED, 'No data found :('))
            return

        all_contents = []
        for sheet_name in sheet_names:
            result = sheet_client.values().get(spreadsheetId=sheet_id, range=sheet_name).execute()
            values = result.get('values', [])
            if is_valid_format(values):
                print(apply_color_and_rest(Fore.LIGHTCYAN_EX, f'Extracted data from sheet: "{sheet_name}"..'))
                all_contents.extend(values[1:]) # exclude header and add to global list
            else:
                print(apply_color_and_rest(Fore.RED, f'Invalid format in sheet: "{sheet_name}". Skipping..'))

        if os.path.exists(TERMY_COMMANDS_FILE) and os.path.isfile(TERMY_COMMANDS_FILE):
            os.remove(TERMY_COMMANDS_FILE)
        file_with_commands = open(TERMY_COMMANDS_FILE, 'w')
        writer = csv.writer(file_with_commands)
        for row in tqdm(all_contents):
            writer.writerow(row)
        file_with_commands.close()
        print(apply_color_and_rest(Fore.LIGHTCYAN_EX, f'Saved data at {TERMY_COMMANDS_FILE}'))
    except ServerNotFoundError as err:
        print(SERVER_ERROR)
    except HttpError as err:
        print(HTPP_SHEET_ERROR)
