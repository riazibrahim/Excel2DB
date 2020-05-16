from app import logger
from app.globalvars import input_folder, input_sheet
from config import Config
from app.helpers import import_excel_to_df
import pandas as pd



# Reading excel using pandas
logger.info('Reading excel using pandas')
file = '/home/soze/coding/26-reportdb/inputs/test.xlsx'
excel_df = import_excel_to_df(filename=file)
logger.info('Successfully imported to dataframe -> rows: {}, columns:{}'.format(len(excel_df), len(excel_df.columns)))
logger.info('Columns identified: {}'.format(excel_df.columns))
