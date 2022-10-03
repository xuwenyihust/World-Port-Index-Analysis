import pandas as pd
from distance import get_distance


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
        .sort_values('distance_in_meters') \
        .head(5)

    print(nearest_ports[["port_name", "distance_in_meters"]])


if __name__ == '__main__':
    main()
