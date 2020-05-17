import argparse
import os
import logging
from config import Config
import sys
from sqlalchemy import create_engine

# Configuring argument options
parser = argparse.ArgumentParser(allow_abbrev=False,
                                 description='A tool for exporting any excel table to an sqlite database by dynamically creating table based on column headers')
# TODO: Give default folder as "inputs"
parser.add_argument('-f', '--folder',
                    dest='input_folder',
                    type=str,
                    help='The folder containing the excel files',
                    required=True)

# TODO: Default Sheet as sheet 1
parser.add_argument('-s', '--sheet',
                    dest='input_sheet',
                    type=str,
                    help='name of the sheet in the Excel workbook to be exported into SQL tables',
                    required=True)

args = parser.parse_args()

# Create directories
if not os.path.exists('logs'):
    os.mkdir('logs')

if not os.path.exists('outputs'):
    os.mkdir('outputs')

# Configure logging #TODO: fancify this, log rotations
# create logger with
logger = logging.getLogger('excel2db')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
file_handler = logging.FileHandler('logs/{}'.format(Config.LOG_FILENAME))
file_handler.setLevel(Config.FILE_LOGGING_LEVEL)
# create console handler with a higher log level
console_handler = logging.StreamHandler()
console_handler.setLevel(Config.CONSOLE_LOGGING_LEVEL)
# create formatter and add it to the handlers
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
console_formatter = logging.Formatter('%(levelname)s: %(message)s')
# console_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
console_handler.setFormatter(console_formatter)
# add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug('Excel2Report app has started')


# SQL configuration

# create engine
dbi_uri = Config.SQLALCHEMY_DATABASE_URI
engine = create_engine(dbi_uri, echo=False)


# Signal handler To exit on Ctrl+C
def signal_handler(sig, frame):
    print('\n\nYou pressed Ctrl+C! .. exiting..')
    sys.exit('Bye!')
