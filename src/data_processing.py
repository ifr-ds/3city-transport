import pandas as pd
import os
from constants import ORIGINS_COORD, time, STOPS_3CITY
from config import TRICITY, logger
from distance_matrix_api import get_time_of_travel


def split_df(data, start, stop):
    df = data.iloc[start:stop, :].copy()
    df['coord'] = df.apply(lambda x: f"{x['stopLat']}, {x['stopLon']}", axis=1)
    return df.sort_values('coord')


def get_zone(result):
    adresses = result['destination_addresses']
    city = [place.split(', ')[1] for place in adresses]

    zones = []
    for z in city:
        element = z.split(' ')
        if len(element) > 1:
            zones.append(element[1])
        else:
            zones.append(element[0])
    return zones


def prepare_stops_to_request(df):
    return [split_df(df, i, i + 100) for i in range(0, len(df), 100)]


def google_api_request(dfs_splited):
    return [get_time_of_travel(
        ORIGINS_COORD, desttination['coord'].to_list(), time)
        for desttination in dfs_splited]


def add_times_of_travels(dfs_splited):
    results = google_api_request(dfs_splited)
    travel_times = [[i['duration']['value']
                     for i in result['rows'][0]['elements']]
                    for result in results]
    return [df.assign(time_sec=time_t)
            for df, time_t in zip(dfs_splited, travel_times)]


def save_times_data():
    df = pd.read_csv(STOPS_3CITY, index_col=0)
    logger.debug("Data readed")

    dfs_splited = prepare_stops_to_request(df)
    logger.debug("Dataframe prepared to request")

    dfs_with_times = add_times_of_travels(dfs_splited)
    logger.debug("Added times of travels to dataframes")

    df_merged = pd.DataFrame()
    for data_part in dfs_with_times:
        df_merged = df_merged.append(df)
    logger.debug("Dataframes prepared to save")

    date = time.strftime('%m-%d-%Y_%H-%M-%S')
    df_merged.to_csv(os.path.join(TRICITY, "data", f"tricity_travel_{date}"))
    logger.debug("Data saved")


if __name__ == "__main__":
    save_times_data()
