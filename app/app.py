from app import logger
from app.globalvars import input_folder, input_sheet


print("Specified input folder is {}".format(input_folder))
print("Specified input sheet is {}".format(input_sheet))

logger.info("Processing completed. Bye!")