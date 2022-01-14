import json
import os
import pickle
import sys

import pandas as pd
from colorama import Fore
from httplib2 import ServerNotFoundError
from rapidfuzz import process, fuzz
import requests
from pkg_resources import parse_version
from datetime import datetime, timedelta
from dateutil import parser
import traceback


from termy.constants import TERMY_COMMANDS_FILE, MATCH_THRESHOLD, CREDS_OBJECT_FILE, CONFIG, TERMY_CONFIGURE_MESSAGE, \
    SHEET_LINK_INPUT, INVALID_SHEET_LINK, STOPWORDS, ColNames, APP_NAME, VERSION, ConfigKeys, \
    GOOGLE_AUTH_PROMPT_ON_UNAUTHORISED_SHEET, SERVER_ERROR, AUTHENTICATION_FAILED_ON_UPDATE_ERROR, \
    SHEET_NOT_FOUND_ERROR, UNKNOWN_EXCEPTION_ERROR
from termy.exception.custom_exceptions import GoogleSheetAuthRequiredException, GoogleSheetNotFoundException, \
    UnknownException
from termy.service.aunthenticator.authenticate import google_auth_renew, connect_to_google_sheet
from termy.service.content_extractor.get_sheet_content import get_sheet_content_into_csv
from termy.service.gpt_client.gpt3_terminal_client import GPT3TerminalClient
from termy.utils import save_object, apply_color_and_rest, save_config


def extract_sheet_id(sheet_link):
    link_parts = sheet_link.split('/')
    if len(link_parts) >= 5:
        return link_parts[5]
    return None


def configure_termy():
    print(apply_color_and_rest(Fore.LIGHTCYAN_EX, f'Configuring Termy...\n'))

    sheet_link = input(SHEET_LINK_INPUT)
    sheet_id = extract_sheet_id(sheet_link)
    if not sheet_id:
        sys.exit(INVALID_SHEET_LINK)

    config = {ConfigKeys.SHEET_ID: sheet_id, ConfigKeys.SHEET_LINK: sheet_link}

    try:
        connect_to_google_sheet(sheet_id)
        config[ConfigKeys.AUTH_REQUIRED] = False
        save_config(config)
        update_termy()
    except GoogleSheetAuthRequiredException:
        auth_prompt_response = input(GOOGLE_AUTH_PROMPT_ON_UNAUTHORISED_SHEET)
        if auth_prompt_response.lower() in ['y', 'yes']:
            creds = google_auth_renew()
            save_object(creds, CREDS_OBJECT_FILE)
            config[ConfigKeys.AUTH_REQUIRED] = True
            save_config(config)
            update_termy()
    except GoogleSheetNotFoundException:
        sys.exit(SHEET_NOT_FOUND_ERROR)
    except ServerNotFoundError:
        sys.exit(SERVER_ERROR)
    except (UnknownException, Exception) as err:
        traceback.print_exc()
        sys.exit(UNKNOWN_EXCEPTION_ERROR)


def check_for_package_updates():
    try:
        response = requests.get(f'https://pypi.org/pypi/{APP_NAME}/json')
        latest_version = response.json()['info']['version']
        if parse_version(VERSION) < parse_version(latest_version):
            print(
                f'\n{Fore.LIGHTYELLOW_EX}You current termy version is {VERSION}. A new version {latest_version} is available.'
                f'\nRecommend you to get the latest version by executing the command {Fore.LIGHTGREEN_EX}pip install -U termy {Fore.RESET}')
    except Exception as e:
        print(
            f'{Fore.LIGHTYELLOW_EX}To make sure you have the latest termy version, execute the command {Fore.LIGHTGREEN_EX}pip install -U termy {Fore.RESET}')


def save_last_updated_date(config):
    config[ConfigKeys.LAST_UPDATED_AT] = datetime.now().isoformat()
    if not ConfigKeys.CHECK_UPDATE_AFTER in config:
        config[ConfigKeys.CHECK_UPDATE_AFTER] = 14

    with open(CONFIG, 'w') as f:
        json.dump(config, f)

    print(apply_color_and_rest(Fore.LIGHTCYAN_EX, f"Saving configurations at {CONFIG}"))


def periodic_update_prompt():
    try:
        if not os.path.exists(CONFIG):
            sys.exit(TERMY_CONFIGURE_MESSAGE)
        with open(CONFIG, 'r') as f:
            config = json.load(f)

        last_updated_date = config.get(ConfigKeys.LAST_UPDATED_AT, None)
        if not last_updated_date:
            return
        last_updated_date = parser.parse(last_updated_date)
        update_period_days = config.get(ConfigKeys.CHECK_UPDATE_AFTER)
        next_update_date = last_updated_date + timedelta(days=update_period_days)
        if datetime.now() > next_update_date:
            response = input(
                f"{Fore.LIGHTYELLOW_EX} It's been more than {update_period_days} days since you last synced your google sheet. Would you like to update and sync the data? (y/n) : {Fore.RESET}")
            if response.lower() in ['y', 'yes']:
                print(apply_color_and_rest(Fore.LIGHTCYAN_EX, f"Executing update command : termy --update"))
                update_termy()
            else:
                print(apply_color_and_rest(Fore.LIGHTYELLOW_EX,
                                           f"Cool, Skipping update. Will ask again in {update_period_days} days. You can change the auto update settings by changing 'check_for_update_after' field in {CONFIG}{Fore.RESET}\n\n"))
                config[ConfigKeys.CHECK_UPDATE_AFTER] = update_period_days * 2
                with open(CONFIG, 'w') as f:
                    json.dump(config, f)

    except Exception as e:
        traceback.print_exc()
        sys.exit(UNKNOWN_EXCEPTION_ERROR)


def update_termy():
    try:
        with open(CONFIG, 'r') as f:
            config = json.load(f)

        auth_creds = None
        if config.get(ConfigKeys.AUTH_REQUIRED, False):
            with open(CREDS_OBJECT_FILE, 'rb') as config_dictionary_file:
                auth_creds = pickle.load(config_dictionary_file)

        sheet_id = config.get(ConfigKeys.SHEET_ID)
        get_sheet_content_into_csv(sheet_id=sheet_id, creds=auth_creds)
        check_for_package_updates()
        save_last_updated_date(config)
    except FileNotFoundError as e:
        sys.exit(TERMY_CONFIGURE_MESSAGE)
    except GoogleSheetAuthRequiredException:
        sys.exit(AUTHENTICATION_FAILED_ON_UPDATE_ERROR)
    except GoogleSheetNotFoundException:
        sys.exit(SHEET_NOT_FOUND_ERROR)
    except ServerNotFoundError:
        sys.exit(SERVER_ERROR)
    except (UnknownException, Exception) as err:
        traceback.print_exc()
        sys.exit(UNKNOWN_EXCEPTION_ERROR)


def execute_command(command):
    print(apply_color_and_rest(Fore.LIGHTCYAN_EX, f'Detected Command : {command}'))
    user_input = input(Fore.LIGHTCYAN_EX + f'Press enter to execute' + Fore.RESET)
    if user_input in ['n', 'no', 'c', 'cancel']:
        print(Fore.RED + 'Abort..')
    else:
        os.system(command)


def remove_stopwords(query):
    tokens = query.split()
    tokens = [token for token in tokens if not token in STOPWORDS]
    return ' '.join(tokens)


def rank_matches(matches, search_text):
    highest_score = matches[0][1]
    if highest_score < MATCH_THRESHOLD:  # low threshold, skip reranking
        return matches[0]

    # reranking logic based on min number of tokens not matched.
    tokens_not_matched_counts = []
    for match in matches[:10]:
        match_score = match[1]
        if match_score != highest_score:
            break
        matched_query = match[0]
        tokens_not_matched_count = 0
        for token in matched_query.split():
            if token not in search_text:
                tokens_not_matched_count += 1
        tokens_not_matched_counts.append(tokens_not_matched_count)

    best_match_index = tokens_not_matched_counts.index(min(tokens_not_matched_counts))
    return matches[best_match_index]


def search_and_execute(search_text):
    commands, queries = load_commands_and_queries()
    search_text = remove_stopwords(search_text)
    matches = process.extract(search_text, queries, scorer=fuzz.token_set_ratio)
    if matches:
        match = rank_matches(matches, search_text)
        match_query, score, index = match
        if score >= MATCH_THRESHOLD:
            command = commands[index]
            execute_command(command)
        else:
            print(apply_color_and_rest(Fore.RED, 'No match found :('))
            print(apply_color_and_rest(Fore.RED,
                                       'Try adding the query and command to the Sheet and do'
                                       + Fore.GREEN + ' termy --update'))
    else:
        print(apply_color_and_rest(Fore.RED, 'No match found :('))
        print(apply_color_and_rest(Fore.RED,
                                   'Try adding the query and command to the Sheet and do '
                                   + Fore.GREEN + ' termy --update'))


def show_configs():
    print('show configs not yet supported')


def load_commands_and_queries():
    try:
        df = pd.read_csv(TERMY_COMMANDS_FILE)
        commands, queries = list(df[ColNames.COMMANDS]), list(df[ColNames.QUERY])
        final_commands, final_queries = [], []
        for i, query in enumerate(queries):
            query_variations = query.split('\n')
            query_variations = [variation for variation in query_variations if variation]
            final_queries.extend(query_variations)
            final_commands.extend([commands[i]] * len(query_variations))
        return final_commands, final_queries
    except FileNotFoundError as e:
        sys.exit(TERMY_CONFIGURE_MESSAGE)


def resolve_command_from_GPT3(query):
    client = GPT3TerminalClient()
    command = client.get_command(query)
    if command:
        execute_command(command)
    else:
        print(apply_color_and_rest(Fore.RED, 'No match found :('))


def display_current_configs():
    if not os.path.exists(CONFIG):
        print(apply_color_and_rest(Fore.RED, 'No config file found, \nTry termy --configure to configure first'))
        return

    with open(CONFIG, 'r') as f:
        config = json.load(f)

    print(apply_color_and_rest(Fore.LIGHTCYAN_EX, 'Current configurations'))
    for key, value in config.items():
        print(apply_color_and_rest(Fore.LIGHTCYAN_EX, f'{key} : {value}'))


if __name__ == '__main__':
    configure_termy()
