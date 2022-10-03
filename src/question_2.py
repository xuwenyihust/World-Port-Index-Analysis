import pandas as pd


def main():
    print(">>> Which country has the largest number of ports with a cargo_wharf?")
    ports = pd.read_csv("./data/world_port_index.csv")
    ports_with_cargo_wharf = ports[ports["cargo_wharf"] == True]

    ports_with_cargo_wharf_per_country = ports_with_cargo_wharf\
        .groupby(["country"])\
        .size()\
        .reset_index(name='port_count')

    res = ports_with_cargo_wharf_per_country[ports_with_cargo_wharf_per_country['port_count'] ==
                                             ports_with_cargo_wharf_per_country['port_count'].max()]

    print(res)


if __name__ == '__main__':
    main()
