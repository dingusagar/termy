import json
import os.path
import csv

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import csv
import requests
import pandas as pd

from termy.constants import TERMY_COMMANDS_FILE


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

        if (os.path.exists(TERMY_COMMANDS_FILE) and os.path.isfile(TERMY_COMMANDS_FILE)):
            os.remove(TERMY_COMMANDS_FILE)
        file_with_commands = open(TERMY_COMMANDS_FILE, 'w')
        writer = csv.writer(file_with_commands)
        for row in values:
            writer.writerow(row)
        file_with_commands.close()
    except HttpError as err:
        print(err)


def get_sheet_content_to_csv(SAMPLE_SPREADSHEET_ID , SAMPLE_RANGE_NAME, API_KEY):
    url = "https://sheets.googleapis.com/v4/spreadsheets/"+SAMPLE_SPREADSHEET_ID +"/values/"+SAMPLE_RANGE_NAME
    params = {"key": API_KEY}
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, params=params, headers=headers)
    final_dictionary = json.loads(response.text)
    if (os.path.exists(TERMY_COMMANDS_FILE) and os.path.isfile(TERMY_COMMANDS_FILE)):
        os.remove(TERMY_COMMANDS_FILE)
    file_with_commands = open(TERMY_COMMANDS_FILE, 'w')
    csv_writer = csv.writer(file_with_commands)

    for emp in final_dictionary.get("values"):
        csv_writer.writerow(emp)
    file_with_commands.close()