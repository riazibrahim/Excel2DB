from app import logger, engine
from app.helpers import import_excel_to_df, update_table_schema, export_df_to_db, select_table_name
from app.globalvars import table_schema_dict, input_folder
from app.models import create_table
import glob
from config import Config
import os

logger.info('Selecting input files')
for file in glob.iglob(os.path.join(input_folder, '*.xls*'), recursive=True):
    print('\n')
    logger.info('++++++++++++++++++++++++++++++++++\nChoosing file: {}'.format(file))
    # Get only the base file name without the extension
    file_name = os.path.basename(file).split('.')[0]
    table_name = select_table_name(file_name)
    logger.info('Chosen table "{}"'.format(table_name))
    # TODO: Handle promotion step and application column difference
    # Read excel using pandas
    logger.debug('Reading excel using pandas')
    excel_df = import_excel_to_df(filename=file)
    if excel_df is False:
        logger.warning('Check logs for error. Skipping current file ...')
        continue
    logger.debug('Successfully imported to dataframe -> rows: {}, columns:{}'.format(len(excel_df), len(excel_df.columns)))
    logger.debug('Columns identified: {}'.format(excel_df.columns))
    # Update database table schema #TODO: do a check, if table exists, before doing this
    logger.debug('Moving on to create database table from dataframe headers...')
    update_table_schema(excel_df=excel_df, table_name=str(table_name))  # TODO: change to zone name
    logger.debug('Created table from the dataframe headers')

    # Create database table in database
    logger.debug('Updated table schema \n{}'.format(table_schema_dict))
    logger.debug('Creating table based on the new schema')
    if not create_table(table_schema_dict):
        logger.warning('Check logs for error. Skipping current file ...')
        continue
    # Dump excel data into the database table
    logger.info('Updating database table with the contents')
    if not export_df_to_db(engine=engine, dataframe=excel_df, tablename=str(table_name)):
        logger.warning('Check logs for error. Skipping current file ...')
        continue
    logger.info('Successfully updated database table with the contents')

