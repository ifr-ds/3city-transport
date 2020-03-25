import os
import logging

TRICITY = os.environ.get('tricity', '~/3city-transport/')
TRICITY_DATA = os.environ.get('tricity_data', '~/3city-transport/src/state')

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)


def configure_logger(filepath: str = None, loglevel=logging.DEBUG):
    logger.setLevel(logging.DEBUG)

    log_format = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] %(message)s'
        #    '[--> %(pathname)s [%(process)d]:]')
    )

    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(loglevel)
    consoleHandler.setFormatter(log_format)

    logger.addHandler(consoleHandler)

    # file logger only on demand

    if filepath:
        fileHandler = logging.FileHandler(filepath)
        fileHandler.setLevel(logging.DEBUG)
        fileHandler.setFormatter(log_format)

        logger.addHandler(fileHandler)

    return logger
