import pandas as pd
import os
from constants import ORIGINS_COORD, time, STOPS_3CITY
from config import TRICITY, logger
from distance_matrix_api import get_time_of_travel


def split_df(data: pd.DataFrame, start: int, stop: int) -> pd.DataFrame:
    """
    return part of dataframe.
    google api allows on 100 coordinates in one request
    """
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


def prepare_stops_to_request(df: pd.DataFrame) -> list:
    """
    return list of splited dataframes
    """
    return [split_df(df, i, i + 100) for i in range(0, len(df), 100)]


def google_api_request(dfs_splited: list) -> list:
    """
    requests to google api in loop by splited dataframes
    """
    return [get_time_of_travel(
        ORIGINS_COORD, desttination['coord'].to_list(), time)
        for desttination in dfs_splited]


def add_times_of_travels(dfs_splited: list) -> list:
    """
    extract time from google api answers
    add results to splited dataframes
    """
    results = google_api_request(dfs_splited)
    logger.debug("Ready answer for request")

    travel_times = [[i['duration']['value']
                     for i in result['rows'][0]['elements']]
                    for result in results]
    logger.debug("Times of travel extracted")

    return [df.assign(time_sec=time_t)
            for df, time_t in zip(dfs_splited, travel_times)]


def save_times_data():
    """
    save data from requests to csv file
    """
    df = pd.read_csv(STOPS_3CITY, index_col=0)
    logger.debug("Data readed")

    dfs_splited = prepare_stops_to_request(df)
    logger.debug("Dataframe prepared to request")

    dfs_with_times = add_times_of_travels(dfs_splited)
    logger.debug("Added times of travels to dataframes")

    df_merged = pd.DataFrame()
    for data_part in dfs_with_times:
        df_merged = df_merged.append(data_part)
    logger.debug("Dataframes prepared to save")

    date = time.strftime('%m-%d-%Y_%H-%M-%S')
    df_merged.to_csv(os.path.join(TRICITY, "data",
                                  f"tricity_travel_{date}.csv"))
    logger.debug("Data saved")


if __name__ == "__main__":
    save_times_data()
