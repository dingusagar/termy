import argparse

# from termy import parser
parser = argparse.ArgumentParser(add_help=False,
                                 description='Termy is a terminal assistant which is focussed on easing out the '
                                             'developers life, by triggering commands just bsaed on the NLI')
from termy.service.service import configure_termy

parser.add_argument("-c", "--configure", type=configure_termy, action="store", help="Configure your termy")
parser.add_argument("-u", "--update", dest="update", help="Update termy to be updated with the latest commands")
parser.add_argument("-s", "--search", dest="search", help="termy will help you to search !!")
parser.add_argument("-show", "--show_configurations", dest="show_configurations", help="View the termy configs")
parser.add_argument("-h", "--help", action="help",
                    help="Termy will ease your job and help you to run any command using NLI")
args = parser.parse_args()
print("args", args)