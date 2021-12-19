import argparse
import sys

from termy.constants import TERMY_INTRO_MESSAGE, VERSION
from termy.service.flow_handler.handle_flows import configure_termy, search_and_execute, update_termy

DESCRIPTION = TERMY_INTRO_MESSAGE


def init_cli_app():
    parser = argparse.ArgumentParser(add_help=False,
                                     description=DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('search', help='Input String', nargs='*')
    parser.add_argument("-c", "--configure", action='store_true', help="Configure your termy")
    parser.add_argument("--show-config", action='store_true', help="Shows the current configurations")
    parser.add_argument("-u", "--update", action='store_true',
                        help="Update termy to be updated with the latest commands")
    parser.add_argument("-v", "--version", action='store_true',
                        help="Version Info")
    args = parser.parse_args()

    if args.search:
        query = ' '.join(args.search)
        search_and_execute(query)
    elif args.configure:
        configure_termy()
    elif args.update:
        update_termy()
    elif args.version:
        print(VERSION)
    else:
        parser.print_help(sys.stdout)


if __name__ == '__main__':
    init_cli_app()
