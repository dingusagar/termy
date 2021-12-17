from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A lightweight terminal assistant to give a natural language interface to your terminal commands'

# Setting up
setup(
    name="termy",
    version=VERSION,
    author="Dingu Sagar, Bhanu Rekha, Divya Priya",
    author_email="<dingusagar@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'pandas==1.3.5',
        'rapidfuzz==1.9.1',
        'google-api-python-client==2.33.0',
        'google-auth-httplib2==0.1.0',
        'google-auth-oauthlib==0.4.6',
        'colorama==0.4.4',
        'tqdm==4.62.3',
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
