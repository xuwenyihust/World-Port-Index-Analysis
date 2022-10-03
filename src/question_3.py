import pandas as pd
from distance import get_distance


def main():
    print(">>> Distress call response")
    ports = pd.read_csv("./data/world_port_index.csv")

    ports["distance_in_meters"] = ports.apply(lambda x: get_distance(x["port_latitude"],
                                                                     32.610982,
                                                                     x["port_longitude"],
                                                                     -38.706256), axis=1)
    ports_with_supplies = ports[(ports["provisions"] == True) &
                                (ports["water"] == True) &
                                (ports["fuel_oil"] == True) &
                                (ports["diesel"] == True)]

    res = ports_with_supplies \
        .sort_values('distance_in_meters') \
        .head(1)[["country", "port_name", "port_latitude", "port_longitude"]]

    print(res)


if __name__ == '__main__':
    main()
