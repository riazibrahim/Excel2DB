from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app.globalvars import table_schema_dict
from app.helpers import create_table_schema
from app import engine

# Obtain the table schema
table_schema = create_table_schema()

# Create table from db_schema dict
Base = declarative_base()
SampleTableClass = type('SampleTableClass', (Base,), table_schema)
Base.metadata.create_table(engine)
