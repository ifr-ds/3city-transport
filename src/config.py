import os
import logging

TRICITY = os.environ.get('tricity', '~/3city-transport/')
TRICITY_DATA = os.environ.get('tricity_data', '~/3city-transport/src/state')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
