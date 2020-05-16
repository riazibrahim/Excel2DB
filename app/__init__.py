import argparse
import os
import logging
from config import Config
import sys


# Configuring argument options
parser = argparse.ArgumentParser(allow_abbrev=False, description='A tool for exporting an excel to an sqlite database by dynamically creating table')
#TODO: Give default folder as "inputs"
parser.add_argument('-f', '--folder',
                    dest='folder_name',
                    type=str,
                    help='point to the folder containing the excel files',
                    required=False)

parser.add_argument('-s', '--sheet',
                    dest='sheet_name',
                    type=str,
                    help='Sheet name in Excel to be coverted to SQL tables',
                    required=False)


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


# Signal handler To exit on Ctrl+C
def signal_handler(sig, frame):
    print('\n\nYou pressed Ctrl+C! .. exiting..')
    sys.exit('Bye!')