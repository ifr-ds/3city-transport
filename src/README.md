# Connection 

### googlemaps python library

Request example:
```
import googlemaps
from datetime import datetime

time = datetime.now()
gmaps = googlemaps.Client(key=API_KEY)

distance_result = gmaps.distance_matrix(
                                    
                        origins='Niedźwiednik 01, 80-292 Gdańsk',
                        destinations=['Miszewskiego 02, Gdańsk', 
                                      'Gdańsk Przymorze - Uniwer, Malborska, 80-309 Gdańsk'],
                        mode='transit',
                        units='metrics',
                        departure_time=time,
                        traffic_model='best_guess'
                        )
```

Answer example:
```
{'destination_addresses': ['Miszewskiego 02, Gdańsk, Poland',
  'Gdańsk Przymorze - Uniwer, Malborska, 80-309 Gdańsk, Poland'],
 'origin_addresses': ['Niedźwiednik 01, 80-292 Gdańsk, Poland'],
 'rows': [{'elements': [{'distance': {'text': '4.5 km', 'value': 4520},
     'duration': {'text': '33 mins', 'value': 1989},
     'status': 'OK'},
    {'distance': {'text': '4.2 km', 'value': 4218},
     'duration': {'text': '28 mins', 'value': 1672},
     'status': 'OK'}]}],
 'status': 'OK'}
 ```
 **Note:
more useful is insertion origin and destinations by coordinates**