from sqlalchemy.ext.declarative import declarative_base
from app import engine, logger


# Create table from db_schema dict
def create_table(table_schema_dict):
    logger.info('Initializing Base')
    Base = declarative_base()
    logger.info('Dynamically generating Table Class')
    SampleTableClass = type('SampleTableClass', (Base,), table_schema_dict)

    logger.info('Generating all tables')
    Base.metadata.create_all(engine)
