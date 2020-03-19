import googlemaps
from src.secrets import API_KEY


def get_time_of_travel(origins_coord, dest_coord, time):
    gmaps_cli = googlemaps.Client(key=API_KEY)

    result = gmaps_cli.distance_matrix(
        origins=origins_coord,
        destinations=dest_coord,
        mode='transit',
        units='metrics',
        departure_time=time,
        traffic_model='best_guess')

    return result
