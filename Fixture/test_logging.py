import logging


def test_logging():
    logger = logging.getLogger(__name__)
    file = logging.FileHandler('loger1.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    file.setFormatter(formatter)
    fileHandler = logger.addHandler(file)
    logger.setLevel(logging.CRITICAL)
    logger.debug("A debug statement is executed")
    logger.info("Information statement is executed")
    logger.warning("look at warning messabges")
    logger.error("There is error message")
    logger.critical("A critical statement is present")
