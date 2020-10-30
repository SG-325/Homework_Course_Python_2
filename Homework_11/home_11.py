import logging
from random import randint


for i in range(50):
	num = randint(0,50)
	print(num)

	if num < 10:
		logging.basicConfig(filename = "T.log", format = "%(levelname)s:%(asctime)s:%(message)s", level = logging.DEBUG)
	
	elif num < 20:
		logging.basicConfig(filename = "T.log", format = "%(levelname)s:%(asctime)s:%(message)s", level = logging.INFO)

	elif num < 30:
		logging.basicConfig(filename = "T.log", format = "%(levelname)s:%(asctime)s:%(message)s", level = logging.WARNING)

	elif num < 40:
		logging.basicConfig(filename = "T.log", format = "%(levelname)s:%(asctime)s:%(message)s", level = logging.ERROR)
		
	else:
		logging.basicConfig(filename = "T.log", format = "%(levelname)s:%(asctime)s:%(message)s", level = logging.CRITICAL)



	logging.debug(f"This is the debug level. We generate a random number and that number is {num}.")
	logging.info(f"This is the info level, the number is {num}.")
	logging.warning("This is the warning level, because the generate number is less than 30")
	logging.error('This is the error level, because the generating number is less than 40.')
	logging.critical("This is the critical level, because  generating number less 50.")









