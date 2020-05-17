from sqlalchemy.ext.declarative import declarative_base
from app import engine, logger
import sys


# Create table from db_schema dict
def create_table(table_schema_dict):
    try:
        logger.debug('Entered ::: create_table')
        logger.debug('table schema passed is \n{}'.format(table_schema_dict))
        logger.debug('Initializing Base')
        Base = declarative_base()
        logger.debug('Dynamically generating Table Class')
        SampleTableClass = type('SampleTableClass', (Base,), table_schema_dict)
        logger.info('Generating table')
        Base.metadata.create_all(engine)
        logger.debug('Cleaning table schema dictionary...')
        table_schema_dict.clear()
    except Exception as ex:
        logger.warning('Fatal Error! {}'.format(ex))
        sys.exit('Bye!')
