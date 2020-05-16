from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app.globalvars import table_schema_dict
from app.helpers import create_table_schema
from app import engine, logger

# Obtain the table schema
logger.info('Getting table schema')
table_schema_dict = create_table_schema()
logger.info('Table schema is {}'.format(table_schema_dict))


# Create table from db_schema dict
logger.info('Initializing Base')
Base = declarative_base()
logger.info('Dynamically generating Table Class')
SampleTableClass = type('SampleTableClass', (Base,), table_schema_dict)

logger.info('Generating all tables')
Base.metadata.create_all(engine)
