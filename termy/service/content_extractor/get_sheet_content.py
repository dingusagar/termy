import csv
import os.path

from colorama import Fore

from termy.constants import TERMY_COMMANDS_FILE, ColNames, EMPTY_SHEET_MESSAGE
from termy.service.aunthenticator.authenticate import connect_to_google_sheet
from termy.utils import apply_color_and_rest


def is_valid_format(values):
    if not values:
        return False

    header = values[0]
    if ColNames.QUERY in header and ColNames.COMMANDS in header:
        return True

    return False


def save_to_csv(all_contents, header):
    file_with_commands = open(TERMY_COMMANDS_FILE, 'w')
    writer = csv.writer(file_with_commands)
    writer.writerow(header)
    for row in all_contents:
        writer.writerow(row)
    file_with_commands.close()


def get_sheet_content_into_csv(sheet_id, creds):
    sheet_client, sheet_metadata = connect_to_google_sheet(sheet_id, creds)
    sheets = sheet_metadata.get('sheets', '')
    sheet_names = [sheet['properties']['title'] for sheet in sheets]

    if not sheet_names:
        print(apply_color_and_rest(Fore.RED, 'No data found :('))
        return

    all_contents = []
    header = None
    for sheet_name in sheet_names:
        result = sheet_client.values().get(spreadsheetId=sheet_id, range=sheet_name).execute()
        values = result.get('values', [])
        if is_valid_format(values):
            print(apply_color_and_rest(Fore.LIGHTCYAN_EX, f'Downloading data from sheet: "{sheet_name}"..'))
            header, contents = values[0], values[1:]
            contents = [content for content in contents if content]
            all_contents.extend(contents) # exclude header and add to global list
        else:
            print(apply_color_and_rest(Fore.RED, f'Invalid format in sheet: "{sheet_name}". Skipping..'))

    if os.path.exists(TERMY_COMMANDS_FILE) and os.path.isfile(TERMY_COMMANDS_FILE):
        os.remove(TERMY_COMMANDS_FILE)
    if all_contents:
        save_to_csv(all_contents, header)
        print(apply_color_and_rest(Fore.LIGHTCYAN_EX, f'Saving data at {TERMY_COMMANDS_FILE}'))
    else:
        print(EMPTY_SHEET_MESSAGE)