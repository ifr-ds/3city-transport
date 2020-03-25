import os
from datetime import datetime
from config import TRICITY_DATA

ORIGINS_COORD = '54.38, 18.55937'

STOPS_3CITY = os.path.join(TRICITY_DATA, 'stops_3city_checked.csv')

time = datetime.now()
