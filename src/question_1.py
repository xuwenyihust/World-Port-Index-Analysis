import pandas as pd
from math import radians, cos, sin, asin, sqrt


def main():
    print(">>> What are the 5 nearest ports to Singapore's JURONG ISLAND port?")
    data = pd.read_csv("./data/world_port_index.csv")

    jurong_island = data[(data["country"] == 'SG') & (data["port_name"] == "JURONG ISLAND")]
    jurong_island_index = jurong_island.iloc[0]["index_number"]
    jurong_island_latitude = jurong_island.iloc[0]["port_latitude"]
    jurong_island_longitude = jurong_island.iloc[0]["port_longitude"]

    # distance_in_meters --> distance_in_meters_to_jurong_island
    data["distance_in_meters"] = data.apply(lambda x: get_distance(x["port_latitude"],
                                                                   jurong_island_latitude,
                                                                   x["port_longitude"],
                                                                   jurong_island_longitude), axis=1)

    nearest_ports = data[data["index_number"] != jurong_island_index] \
        .sort_values('distance_in_meters')\
        .head(5)

    print(nearest_ports[["port_name", "distance_in_meters"]])


def get_distance(lat1, lat2, lon1, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    c = 2 * asin(sqrt(a))
    r = 6371

    return c * r * 1000


if __name__ == '__main__':
    main()
