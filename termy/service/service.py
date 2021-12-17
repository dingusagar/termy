import os
from termy.constants import TERMY_DIR, TERMY_COMMANDS_FILE, MATCH_THRESHOLD
import pandas as pd
from rapidfuzz import process, fuzz

from termy.service.AuthGoogle import google_auth
from termy.service.get_sheet_content import get_sheet_content_into_csv

creds = None
sheet_id = None
sheet_name = None

def configure_termy():
    global creds
    global sheet_name
    global sheet_id
    print('Configuration')
    sheet_id = input('Please enter the Sheet ID for the google sheet that contains the commands data : ')
    sheet_name = input('Please enter the Sheet Name for the google sheet that contains the commands data : ')
    print(f'Configuring , DOC_KEY : {sheet_id}')
    creds = google_auth()
    print(creds)
    update_termy()


def update_termy():
    print('updating data...')
    get_sheet_content_into_csv(sheet_id, sheet_name, creds)


def execute_command(command):
    print(f'Detected Command : {command}')
    user_input = input(f'Press enter to execute')
    if user_input in ['n', 'no', 'c', 'cancel']:
        print('Abort..')
    else:
        print('Executing command...')
        os.system(command)


def search_and_execute(search_text):
    print(f'search : {search_text}')
    commands, queries = load_commands_and_queries()
    match = process.extractOne(search_text, queries, scorer=fuzz.token_set_ratio)
    if match:
        match_query, score, index = match
        if score > MATCH_THRESHOLD:
            command = commands[index]
            execute_command(command)
        else:
            print('No match found :(')
    else:
        print('No match found :(')


def show_configs():
    print('show configs not yet supported')


def load_commands_and_queries():
    df = pd.read_csv(TERMY_COMMANDS_FILE)
    return list(df['commands']), list(df['query'])


if __name__ == '__main__':
    configure_termy()