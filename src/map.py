import folium
import os
import pandas as pd
from config import TRICITY_DATA, TRICITY_STATE, logger
from constants import ORIGINS_COORD


def plot_choropleth(origins: list, city_geo: str, values: pd.DataFrame):
    origins_coord = [float(coord) for coord in origins.split(', ')]

    map3city = folium.Map(location=origins_coord, zoom_start=10)

    folium.Choropleth(
        geo_data=city_geo,
        name='choropleth',
        data=values,
        columns=['id', 'time_min'],
        key_on='feature.id',
        line_weight=2,
        fill_color='YlOrRd',
        fill_opacity=0.4,
        line_opacity=0.2,
        legend_name='Time (min)',
        bins=9,
        reset=True
    ).add_to(map3city)

    map3city.save(os.path.join(TRICITY_DATA, "folium_choropleth_3city.html"))
    logger.info("saved map")


def make_plot():
    """
    city_geo: path to geoJson file with city mesh coordinates
    time_data: pandas dataframe with travel time information
    """
    city_geo = os.path.join(TRICITY_STATE, "geoJson_3city_boundary.json")

    time_data = pd.read_csv(
        os.path.join(TRICITY_DATA,
                     "tricity_travel_03-25-2020_19-41-12.csv"), index_col=0)

    time_data['time_min'] = time_data['time_sec'] / 60

    values = time_data.reset_index(drop=True).rename(columns={'coord': 'id'})

    plot_choropleth(ORIGINS_COORD, city_geo, values)


if __name__ == "__main__":
    make_plot()
