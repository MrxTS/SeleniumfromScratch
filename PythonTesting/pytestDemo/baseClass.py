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
        logger.debug("A debugd statement is executed")
        logger.info("Informationd statement")
        logger.warning("Somethingd is in warning mode")
        logger.error("A Major error has happened")
        logger.critical("Critical issue")
        logger.setLevel(logging.INFO)
        logger.debug("A debugd statement is executed")
        logger.info("Informationd statement")
        logger.warning("Somethingd is in warning mode")
        logger.error("A Major error has happened")
        logger.critical("Critical issue")
        return logger