import inspect
import logging

class baseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.INFO)
        logger.debug("A debudfggd statement is executed")
        logger.info("Informatidfgond statement")
        logger.warning("Somethdfgingd is in warning mode")
        logger.error("A Majordfg error has happened")
        logger.critical("Critdfgical issue")
        logger.setLevel(logging.INFO)
        logger.debug("A debugddfg statement is executed")
        logger.info("Informatidfgond statement")
        logger.warning("Somethdfgingd is in warning mode")
        logger.error("A Major dfgerror has happened")
        logger.critical("Criticadfgl issue")
        return logger