from app import args, logger
from datetime import datetime

filename_prepend = datetime.now().strftime("%Y%m%d-%H%M%S")
# Gather all arguments
logger.debug('Obtaining all arguments')
# input_file = args.file #TODO
input_folder = args.input_folder
input_sheet = args.input_sheet