from app import logger
from app.globalvars import table_schema_dict
import pandas as pd
import sys
from app.globalvars import input_sheet
from sqlalchemy import Column, String, Integer
from config import Config


def update_table_schema(excel_df, zone_name):
    logger.debug('Cleaning table schema dictionary...')
    table_schema_dict.clear()
    logger.debug('Updating table schema dictionary')
    table_schema_dict.update({'__tablename__': zone_name})
    table_schema_dict.update({'id': Column(Integer, primary_key=True)})
    for cols in excel_df.columns:
        table_schema_dict.update({str(cols): Column(String)})
    logger.debug('Final table schema is \n{}'.format(table_schema_dict))
    return table_schema_dict


# Use pandas to load an excel into dataframe
def import_excel_to_df(filename):
    try:
        logger.debug('Reading from excel {}'.format(filename))
        df = pd.read_excel(filename, sheet_name=input_sheet, header=0)
        logger.debug('Dataframe columns names for "{}" is \n{}'.format(filename, df.columns))
        if any("Unnamed" in headings for headings in df.columns):
            logger.debug('Dataframe contains blank rows for contents from file "{}": \n{}'.format(filename, df))
            logger.debug('Dropping all empty rows from database')
            df = df.dropna()
            logger.debug('Setting header row as first non empty row')
            new_header = df.iloc[0]  # grab the first row for the header
            df = df[1:]  # take the data less the header row
            df.columns = new_header  # set the header row as the df header
    except Exception as ex:
        logger.warning('Couldn\'t read file {}\n Error is : {}'.format(filename, ex))
        sys.exit('Fatal Error! Exiting!')  # TODO move return
    logger.debug('Resulting dataframe \n{}'.format(df))
    return df


def export_df_to_db(tablename, engine, dataframe):
    try:
        dataframe.to_sql(name=tablename, con=engine, if_exists='append', index=False)
    except Exception as ex:
        sys.exit('Fatal Error! \n {}'.format(ex))


def select_table_name(file_name):
    # Check if rules dict is populated, else put table name as the file name itself
    logger.info('Identifying table name...')
    if bool(Config.TABLE_NAMES_DICT):
        logger.debug('Table names dict is not empty. Proceeding to identify table name...')
        value = [val for key, val in Config.TABLE_NAMES_DICT.items() if key in file_name]
        if len(value) == 0:
            logger.debug('Key not found')
            table_name = file_name
            logger.debug('Chosen table_name is "{}" for file "{}" '.format(table_name, file_name))
        else:
            table_name = str(value).strip('[\'\']')
            logger.debug('Chosen table_name is "{}" for file "{}" '.format(table_name, file_name))
    else:
        logger.info('Table name selection dict is empty')
        table_name = file_name
        logger.debug('Chosen table_name is "{}" for file "{}" '.format(table_name, file_name))
    return table_name
