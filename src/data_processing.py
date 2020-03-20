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
