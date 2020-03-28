import os
from datetime import datetime
from config import TRICITY_STATE

# origins coordinates of "Dworzec Główny"
ORIGINS_COORD = '54.35483000000001, 18.64512'

STOPS_3CITY = os.path.join(TRICITY_STATE, 'stops_3city_checked.csv')

time = datetime.now()
