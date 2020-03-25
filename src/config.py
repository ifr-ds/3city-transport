import os
import logging

TRICITY = os.environ.get('TRICITY', '~/3city-transport/')
TRICITY_DATA = os.environ.get('TRICITY_DATA', '~/3city-transport/data/')
TRICITY_STATE = os.environ.get('TRICITY_STATE', '~/3city-transport/src/state/')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
