from setuptools import setup, find_packages
import codecs
import os

from termy.constants import VERSION

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

DESCRIPTION = 'A lightweight terminal assistant to give a natural language interface to your terminal commands'

# Setting up
setup(
    name="termy",
    version=VERSION,
    author="Dingu Sagar, Bhanu Rekha, Divya Priya",
    author_email="<termydbd@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'pandas',
        'rapidfuzz',
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib',
        'colorama',
        'tqdm',
        'cryptography',
        'art',
        'openai',
    ],
    keywords=['python', 'termy', 'terminal assistant', 'terminast', 'terminal alias', 'command automation'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
        'console_scripts': ['termy=termy.controller.controller:init_cli_app'],
    }
)
