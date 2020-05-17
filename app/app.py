from app import logger, engine
from app.helpers import import_excel_to_df, update_table_schema, export_df_to_db
from app.globalvars import table_schema_dict, input_folder
from app.models import create_table
import glob
import sys
import os

# TODO: Handle promotion step and application column difference
# Read excel using pandas
logger.info('Reading excel using pandas')
file = '/home/soze/coding/26-reportdb/inputs/test2.xlsx'
excel_df = import_excel_to_df(filename=file)
logger.debug('Successfully imported to dataframe -> rows: {}, columns:{}'.format(len(excel_df), len(excel_df.columns)))
logger.debug('Columns identified: {}'.format(excel_df.columns))

logger.info('Selecting input files')
for file in glob.iglob(os.path.join(input_folder, '*.xls*'), recursive=True):
    print(file)

sys.exit('Bye!') #TODO remove


# Update database table schema #TODO: do a check, if table exists, before doing this
logger.debug('Moving on to create database table from dataframe headers...')
update_table_schema(excel_df=excel_df, zone_name='test') # TODO: change to zone name
logger.debug('Created table from the dataframe headers')

# Create database table in database
logger.debug('Updated table schema \n{}'.format(table_schema_dict))
logger.debug('Creating table based on the new schema')
create_table(table_schema_dict)


# Dump excel data into the database table
logger.info('Updating database table with the contents')
export_df_to_db(engine=engine, dataframe=excel_df, tablename='test')
logger.info('Successfully updated database table with the contents')


