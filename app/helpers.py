from app import logger
from app.globalvars import table_schema_dict
import pandas as pd
import sys
from app.globalvars import input_sheet
from sqlalchemy import Column, String, Integer


def update_table_schema(excel_df, zone_name):
    logger.info('Cleaning table schema dictionary...')
    table_schema_dict.clear()
    logger.info('Updating table schema dictionary')
    table_schema_dict.update({'__tablename__': zone_name})
    table_schema_dict.update({'id': Column(Integer, primary_key=True)})
    for cols in excel_df.columns:
        table_schema_dict.update({str(cols): Column(String)})
    return table_schema_dict


# Use pandas to load an excel into dataframe
def import_excel_to_df(filename):
    try:
        logger.debug('Reading from excel {}'.format(filename))
        df = pd.read_excel(filename, sheet_name=input_sheet, header=None)
        logger.debug('Dropping all empty rows from database')
        df = df.dropna()
        logger.debug('Setting header row as first non empty row')
        header_row = 0
        df.columns = df.iloc[header_row]
    except Exception as ex:
        logger.warning('Couldn\'t read file {}\n Error is : {}'.format(filename, ex))
        sys.exit('Fatal Error! Exiting!')
    return df


def export_df_to_db(tablename, engine, dataframe):
    try:
        dataframe.to_sql(name=tablename, con=engine, if_exists='append', index=False)
    except Exception as ex:
        sys.exit('Fatal Error! \n {}'.format(ex))
