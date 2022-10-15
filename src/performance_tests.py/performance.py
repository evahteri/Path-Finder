
from get_all_paths import Get_All_Paths


def main():
    current_map = open("../Path_Finder/src/static/maps/map_1.txt", "r")
    map = current_map.read().splitlines()
    all_paths = Get_All_Paths().get_all_paths(map)
    print(all_paths)


if __name__ == "__main__":
    main()
