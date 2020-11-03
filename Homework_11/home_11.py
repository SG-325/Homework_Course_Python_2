import logging
from random import randint

logging.basicConfig(filename = "T.log", format = "%(levelname)s:%(asctime)s:%(message)s", level = logging.DEBUG)

for i in range(50):
	num = randint(0,50)

	if num < 10:
		logging.debug(f"This is the debug level. We generate a random number and that number is {num}.")
		logging.info(f"This is the info level, the number is {num}.")
		logging.warning("This is the warning level, because the generate number is less than 30")
		logging.error('This is the error level, because the generating number is less than 40.')
		logging.critical("This is the critical level, because  generating number less 50.")
	
	elif num < 20:
		logging.info(f"This is the info level, the number is {num}.")
		logging.warning("This is the warning level, because the generate number is less than 30")
		logging.error('This is the error level, because the generating number is less than 40.')
		logging.critical("This is the critical level, because  generating number less 50.")

	elif num < 30:
		logging.warning("This is the warning level, because the generate number is less than 30")
		logging.error('This is the error level, because the generating number is less than 40.')
		logging.critical("This is the critical level, because  generating number less 50.")

	elif num < 40:
		logging.error('This is the error level, because the generating number is less than 40.')
		logging.critical("This is the critical level, because  generating number less 50.")
		
	else:
		logging.critical("This is the critical level, because  generating number less 50.")









