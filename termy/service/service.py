import os
from termy.config import TERMY_DIR, TERMY_COMMANDS_FILE, MATCH_THRESHOLD
import pandas as pd
from rapidfuzz import process, fuzz


def configure_termy(a):
    print('Configuration')
    api_key = input('Please enter the API_KEY for the google sheet that contains the commands data : ')
    doc_id = input('Please enter the DOC Key for the google sheet that contains the commands data : ')
    print(f'Configuring API_KEY = {api_key} , DOC_KEY : {doc_id}')



def update_termy():
    print('update yet to be supported')


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