import os
import logging


basedir = os.getcwd()

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///'+os.path.join(basedir, 'reports.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FILE_LOGGING_LEVEL = logging.DEBUG
    CONSOLE_LOGGING_LEVEL = logging.INFO
    LOG_FILENAME = 'excel2db.log'


    # Multiprocessing #TODO
    MAX_THREAD_COUNT = 15
