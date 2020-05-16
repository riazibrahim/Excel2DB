from app import args, logger
from datetime import datetime
from sqlalchemy import Column, Integer, String

filename_prepend = datetime.now().strftime("%Y%m%d-%H%M%S")
# Gather all arguments
logger.debug('Obtaining all arguments')
# input_file = args.file #TODO
input_folder = args.input_folder
input_sheet = args.input_sheet

# table schema skeleton dict
table_schema_dict = {
        '__tablename__': 'sample_table',
        'id': Column(Integer, primary_key=True),
    }
