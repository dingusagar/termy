import csv
import os.path

from colorama import Fore
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from tqdm import tqdm

from termy.constants import TERMY_COMMANDS_FILE


def get_sheet_content_into_csv(SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, creds):
    try:
        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print(Fore.RED + 'No data found')
            return

        if os.path.exists(TERMY_COMMANDS_FILE) and os.path.isfile(TERMY_COMMANDS_FILE):
            os.remove(TERMY_COMMANDS_FILE)
        file_with_commands = open(TERMY_COMMANDS_FILE, 'w')
        writer = csv.writer(file_with_commands)
        for row in tqdm(values, desc="Updating Data ", colour='#32CD32'):
            writer.writerow(row)
        file_with_commands.close()
        print(Fore.LIGHTCYAN_EX + f'Saving data at {TERMY_COMMANDS_FILE}')
    except HttpError as err:
        print(err)
