import os
from datetime import datetime
from config import TRICITY_STATE

ORIGINS_COORD = '54.38, 18.55937'

STOPS_3CITY = os.path.join(TRICITY_STATE, 'stops_3city_checked.csv')

time = datetime.now()
