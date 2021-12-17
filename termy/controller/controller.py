import argparse
import sys

from colorama import Fore

from termy.service.service import configure_termy, search_and_execute, update_termy

DESCRIPTION = Fore.LIGHTYELLOW_EX + '''
Termy is a terminal assistant which is focussed on easing out the developers life
by triggering commands just based on the Natural language.

If you have any feedbacks on this tool, please use this form : https://forms.gle/8sHNPD9PNyVupFht8
You can also visit our github page and raise issues there. : https://github.com/dingusagar/termy
'''


def init_cli_app():
    parser = argparse.ArgumentParser(add_help=False,
                                     description=DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('search', help='Input String', nargs='*')
    parser.add_argument("-c", "--configure", action='store_true', help="Configure your termy")
    parser.add_argument("--show-config", action='store_true', help="Shows the current configurations")
    parser.add_argument("-u", "--update", action='store_true',
                        help="Update termy to be updated with the latest commands")
    args = parser.parse_args()

    if args.search:
        query = ' '.join(args.search)
        search_and_execute(query)
    elif args.configure:
        configure_termy()
    elif args.update:
        update_termy()
    else:
        parser.print_help(sys.stdout)


if __name__ == '__main__':
    init_cli_app()
