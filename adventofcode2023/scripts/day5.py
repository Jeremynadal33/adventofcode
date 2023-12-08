import time
from commons.utils import args, logging
import pandas as pd


def main():
    file_path = (
        f"adventofcode{args.YEAR}/inputs/input_day{args.DAY}.txt"
        if args.INPUT == "REAL"
        else f"adventofcode{args.YEAR}/inputs/test_day{args.DAY}.txt"
    )
    solve_puzzle(input_file=file_path, part=args.PART)


def solve_puzzle(input_file, part):
    logging.info(f"Solving puzzle part {args.PART}")
    if part == 1:
        solve_part_1(input_file)
    elif part == 2:
        solve_part_2(input_file)


def create_maps(file):
    maps = []

    for item in file:
        lines = item.split("\n")
        _map = {}
        _map["source"] = lines[0].split("-")[0]
        _map["destination"] = lines[0].split(" ")[0].split("-")[-1]
        items = []
        for line in lines[1:]:
            numbers = line.split()
            item = {
                "source_start": int(numbers[1]),
                "destination_start": int(numbers[0]),
                "range_length": int(numbers[2]),
            }
            items.append(item)

        df = pd.DataFrame(
            items, columns=["source_start", "destination_start", "range_length"]
        )
        df.sort_values("source_start", inplace=True)
        _map["source_starts"] = df["source_start"].values
        _map["destination_starts"] = df["destination_start"].values
        _map["range_lengths"] = df["range_length"].values
        maps.append(_map)
    return maps


def get_current_map(current_type, maps):
    _map = next(c for c in maps if current_type == c["source"])
    return _map


def look_for_next_number(current_type, current_number, maps):
    """
    Returns next_number, next_source_type
    """
    current_map = get_current_map(current_type, maps)
    # print(current_number, current_map)
    # look what range it corresponds
    if (
        current_number < current_map["source_starts"][0]
        or current_number
        >= current_map["source_starts"][-1] + current_map["range_lengths"][-1]
    ):
        # if not in ranges
        next_number = current_number
        # print('\ncurrent number not in range ', current_number)
    else:
        index = 0
        while (
            current_number
            >= current_map["source_starts"][index] + current_map["range_lengths"][index]
        ):
            # looking for the right range
            index += 1
        next_number = current_map["destination_starts"][index] + (current_number - current_map["source_starts"][index])
        # print('\ndest_start ', current_map["destination_starts"][index])
    # print(current_map["destination"], next_number)
    return next_number, current_map["destination"]

def location(current_type, current_number, maps):
    current_number, current_type = look_for_next_number(current_type, current_number, maps)
    # print(current_number, current_type)
    if current_type == "location":
        # print(current_number)
        return current_number
    else:
        location(current_type, current_number, maps)

def solve_part_1(input_file):
    file = open(input_file, "r").read().split("\n\n")
    seeds = [
        int(item)
        for item in file[0].split(":")[1].strip().replace("  ", " ").split(" ")
    ]
    # print(seeds)

    maps = create_maps(file[1:])
    locations = []
    for seed in seeds:
        current_type = "seed"
        current_number = seed
        # print("\n\nfor seed", seed)
        while current_type != "location":
            current_number, current_type = look_for_next_number(current_type, current_number, maps)
            # print(current_number, current_type)
        # print(current_number)
        locations.append(current_number)
    print(len(locations))
    print(min(locations))


def solve_part_2(input_file):
    file = open(input_file, "r").read().split("\n")


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    logging.info(f"Elapsed in {1000*(end-start)} secondes")
