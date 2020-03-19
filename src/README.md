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

Example of map:

```
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap

output_file("gmap.html")

map_options = GMapOptions(lat=30.2861, lng=-97.7394, map_type="roadmap", zoom=11)

p = gmap(API_KEY, map_options, title="Austin")

source = ColumnDataSource(
    data=dict(lat=[ 30.29,  30.20,  30.29],
              lon=[-97.70, -97.74, -97.78],
              color=["blue","red","black"])
)

p.circle(x="lon", y="lat", size=15, fill_color="color", fill_alpha=0.8, source=source)

show(p)
```
