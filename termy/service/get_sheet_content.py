import os.path

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import csv

from termy.service import Constants


def get_sheet_content_into_csv(SAMPLE_SPREADSHEET_ID , SAMPLE_RANGE_NAME, creds):

    try:
        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found')
            return

        if (os.path.exists(Constants.COMMANDS_CSV_PATH) and os.path.isfile(Constants.COMMANDS_CSV_PATH)):
            os.remove(Constants.COMMANDS_CSV_PATH)
        file_with_commands = open(Constants.COMMANDS_CSV_PATH, 'w')
        writer = csv.writer(file_with_commands)
        for row in values:
            writer.writerow(row)
            print(row)
        file_with_commands.close()
    except HttpError as err:
        print(err)
