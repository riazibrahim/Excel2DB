from app import logger
from app.globalvars import table_schema_dict
import pandas as pd
import sys
from app.globalvars import input_sheet


def create_table_schema():
    return table_schema_dict


# Use pandas to load an excel into dataframe
def import_excel_to_df(filename):
    df = 'test'
    try:
        logger.debug('Reading from excel {}'.format(filename))
        df = pd.read_excel(filename, sheet_name=input_sheet)
        logger.debug('Dropping all empty rows from database')
        df = df.dropna()
        logger.debug('Setting header row as first non empty row')
        header_row=0
        df.columns = df.iloc[header_row]
    except Exception as ex:
        logger.warning('Couldn\'t read file {}\n Error is : {}'.format(filename, ex))
        sys.exit('Fatal Error! Exiting!')
    return df

# Use pandas to connect to the database given in argument
# def export_excel_to_db(engine, tablename, outfile, **kwargs):
# logger.debug('Entered :: export_db_to_excel')
# search_tag = kwargs.get('search_tag', None)
# if search_tag is not None:
#     logger.info('Exporting results for search tag :"{}"'.format(search_tag))
#     logger.debug('Reading {} table from database {} into pandas dataframe'.format(tablename, engine))
#     db_dataframe = pd.read_sql_table(table_name=tablename, con=engine)
#     logger.debug('Read to dataframe from database into pandas')
#     if not os.path.exists('outputs'):
#         os.mkdir('outputs')
#     excel_dataframe = db_dataframe[db_dataframe['search_tag'].str.contains(r'\b{}\b'.format(search_tag))]
#     if excel_dataframe.empty:
#         logger.warning('No records with the given search tag!!')
#         sys.exit('Exiting!')
#     else:
#         records_number = excel_dataframe.shape[0]
#         logger.info('Selected {} records for export ...'.format(records_number))
#         logger.info('Generating output in excel format')
#         excel_dataframe.to_excel('outputs/{}.xlsx'.format(outfile))
#         logger.info('Generated {}.xlsx in outputs folder'.format(outfile))
# else:
#     logger.info('No search tag is given. Proceeding to download entire database')
#     logger.debug('Reading {} table from database {} into pandas dataframe'.format(tablename, engine))
#     db_dataframe = pd.read_sql_table(table_name=tablename, con=engine)
#     logger.debug('Read to dataframe from database into pandas')
#     if not os.path.exists('outputs'):
#         os.mkdir('outputs')
#     logger.info('Generating output in excel format\n')
#     db_dataframe.to_excel('outputs/{}.xlsx'.format(outfile))
#     logger.info('Generated {}.xlsx in outputs folder\n'.format(outfile))
