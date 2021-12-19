import json
import os
import pickle
import sys

import pandas as pd
from colorama import Fore
from rapidfuzz import process, fuzz

from termy.constants import TERMY_COMMANDS_FILE, MATCH_THRESHOLD, CREDS_OBJECT_FILE, CONFIG, SHEET_NAME, \
    TERMY_CONFIGURE_MESSAGE, SHEET_ID_INPUT_MESSAGE
from termy.service.aunthenticator.authenticate import google_auth_renew
from termy.service.content_extractor.get_sheet_content import get_sheet_content_into_csv
from termy.utils import save_object, apply_color_and_rest

creds = None
sheet_id = None
sheet_name = None


def configure_termy():
    global creds
    global sheet_name
    global sheet_id
    sheet_id = input(SHEET_ID_INPUT_MESSAGE)
    sheet_name = input(apply_color_and_rest(Fore.LIGHTCYAN_EX,
                                            "Please enter the Sheet Name for the google sheet that "
                                            "contains the commands data (Press enter for default : 'Sheet1'): "))
    if not sheet_name:
        sheet_name = 'Sheet1'
    config = {"sheet_id": sheet_id, "sheet_name": sheet_name}
    with open(CONFIG, 'w') as f:
        json.dump(config, f)
    print(apply_color_and_rest(Fore.LIGHTGREEN_EX, f'Configuring Termy...'))
    creds = google_auth_renew()
    save_object(creds, CREDS_OBJECT_FILE)
    update_termy()


def update_termy():
    try:
        with open(CREDS_OBJECT_FILE, 'rb') as config_dictionary_file:
            creds = pickle.load(config_dictionary_file)
        with open(CONFIG, 'r') as f:
            config = json.load(f)
        get_sheet_content_into_csv(config.get("sheet_id"), config.get("sheet_name", SHEET_NAME), creds)
    except FileNotFoundError as e:
        sys.exit(TERMY_CONFIGURE_MESSAGE)


def execute_command(command):
    print(apply_color_and_rest(Fore.LIGHTCYAN_EX, f'Detected Command : {command}'))
    user_input = input(Fore.LIGHTCYAN_EX + f'Press enter to execute' + Fore.RESET)
    if user_input in ['n', 'no', 'c', 'cancel']:
        print(Fore.RED + 'Abort..')
    else:
        os.system(command)


def search_and_execute(search_text):
    commands, queries = load_commands_and_queries()
    match = process.extractOne(search_text, queries, scorer=fuzz.token_set_ratio)
    if match:
        match_query, score, index = match
        if score > MATCH_THRESHOLD:
            command = commands[index]
            execute_command(command)
        else:
            print(apply_color_and_rest(Fore.RED, 'No match found :('))
            print(apply_color_and_rest(Fore.RED,
                                       'Try adding the query and command to the Sheet and do'
                                       + Fore.GREEN + 'termy --update'))
    else:
        print(apply_color_and_rest(Fore.RED, 'No match found :('))
        print(apply_color_and_rest(Fore.RED,
                                   'Try adding the query and command to the Sheet and do '
                                   + Fore.GREEN + 'termy --update'))


def show_configs():
    print('show configs not yet supported')


def load_commands_and_queries():
    try:
        df = pd.read_csv(TERMY_COMMANDS_FILE)
        return list(df['commands']), list(df['query'])
    except FileNotFoundError as e:
        sys.exit(TERMY_CONFIGURE_MESSAGE)


if __name__ == '__main__':
    configure_termy()
