from app import logger
from app.globalvars import input_folder, input_sheet
from config import Config
from app.helpers import import_excel_to_df, update_table_schema
from app.globalvars import table_schema_dict
from app.models import create_table
from sqlalchemy import Column, String
import pandas as pd

# Reading excel using pandas
logger.info('Reading excel using pandas')
file = '/home/soze/coding/26-reportdb/inputs/test.xlsx'
excel_df = import_excel_to_df(filename=file)
logger.debug('Successfully imported to dataframe -> rows: {}, columns:{}'.format(len(excel_df), len(excel_df.columns)))
logger.debug('Columns identified: {}'.format(excel_df.columns))

logger.info('Moving on to create database table from dataframe headers...')
update_table_schema(excel_df=excel_df, zone_name='test') # TODO: change to zone name
logger.info('Created table from the dataframe headers')

logger.info('Updated table schema \n{}'.format(table_schema_dict))
logger.info('Creating table based on the new schema')
create_table(table_schema_dict)
