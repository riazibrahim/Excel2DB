from sqlalchemy.ext.declarative import declarative_base
from app import engine, logger
import sys


# Create table from db_schema dict
def create_table(table_schema_dict):
    try:
        logger.info('Entered ::: create_table')
        logger.info('table schema passed is \n{}'.format(table_schema_dict))
        logger.info('Initializing Base')
        Base = declarative_base()
        logger.info('Dynamically generating Table Class')
        SampleTableClass = type('SampleTableClass', (Base,), table_schema_dict)
        logger.info('Generating all tables')
        Base.metadata.create_all(engine)
    except Exception as ex:
        logger.warning('Fatal Error! {}'.format(ex))
        sys.exit('Bye!')
