import argparse
import sys

from termy.constants import TERMY_INTRO_MESSAGE, VERSION
from termy.service.flow_handler.handle_flows import configure_termy, search_and_execute, update_termy, \
    resolve_command_from_GPT3, display_current_configs, periodic_update_prompt

DESCRIPTION = TERMY_INTRO_MESSAGE


def init_cli_app():
    parser = argparse.ArgumentParser(add_help=False,
                                     description=DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter,
                                     usage=argparse.SUPPRESS)

    parser.add_argument('search', help='Input query in natural language', nargs='*')
    parser.add_argument("-c", "--configure", action='store_true',
                        help="Configure your termy with the google sheet containing commands")
    parser.add_argument("--show-config", action='store_true', help="Shows the current configurations")
    parser.add_argument("--gpt3", action='store_true',
                        help="Use GPT-3 API to convert any natural language query into a terminal command")
    parser.add_argument("-u", "--update", action='store_true',
                        help="Update termy and sync the latest commands from the google sheet")
    parser.add_argument("-v", "--version", action='store_true',
                        help="Version Info")
    parser.add_argument("-h", "--help", action='store_true',
                        help="How to use Termy")

    args = parser.parse_args()

    if args.gpt3: # gpt3 search query
        if args.search:
            query = ' '.join(args.search)
        else:
            query = ''
        resolve_command_from_GPT3(query)
    elif args.search: # regular search query
        query = ' '.join(args.search)
        periodic_update_prompt()
        search_and_execute(query)
    elif args.configure:
        configure_termy()
    elif args.update:
        update_termy()
    elif args.version:
        print(VERSION)
    elif args.show_config:
        display_current_configs()
    else:
        parser.print_help(sys.stdout)


if __name__ == '__main__':
    init_cli_app()
