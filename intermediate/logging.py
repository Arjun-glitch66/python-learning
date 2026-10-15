import logging
logging.basicConfig(level=logging.WARNING) #the level is warning 
logging.debug("Checking internal values")
logging.info("Program started")
logging.warning("Input might be invalid")
logging.error("Unable to process input")
#warning level outputs 
#WARNING:root:Input might be invalid
#ERROR:root:Unable to process input

import logging
logging.basicConfig(level=logging.ERROR)
try:
    result=10/0
except ZeroDivisionError:
    logging.exception("Division failed")