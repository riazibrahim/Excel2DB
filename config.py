import os
import logging

basedir = os.getcwd()


class Config:
    # SQL Alchemy configurationsls ou
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir,
                                                                                                       'reports.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Logging configurations
    FILE_LOGGING_LEVEL = logging.DEBUG
    CONSOLE_LOGGING_LEVEL = logging.INFO
    LOG_FILENAME = 'excel2db.log'

    # Table name selection dictionary 'Key' corresponds to string to match in filename, 'Value' corresponds to table name chosen
    # TABLE_NAMES_DICT = {}

    TABLE_NAMES_DICT = {
        'NAZ': 'NAZ',
        'MAZ': 'MAZ',
        'SAZ': 'SAZ',
        'APAC': 'APAC',
        'EUR': 'EUR',
        'AFR': 'AFR',
        'GLOBAL': 'GHQ',
    }

    # Multiprocessing #TODO
    MAX_THREAD_COUNT = 15
