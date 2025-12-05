import time
from commons.utils import args, logging


def main():
    file_path = (
        f"adventofcode{args.YEAR}/inputs/input_day{args.DAY}.txt"
        if args.INPUT == "REAL"
        else f"adventofcode{args.YEAR}/inputs/test_day{args.DAY}.txt"
    )
    solve_puzzle(input_file=file_path, part=args.PART)


def solve_puzzle(input_file, part):
    logging.info(f"Solving puzzle part {args.DAY}")
    if part == 1:
        solve_part_1(input_file)
    elif part == 2:
        solve_part_2(input_file)


def solve_part_1(input_file):
    file = open(input_file, "r").read().split("\n\n")

    ranges = [ (int(x), int(y)) for x, y in (line.split('-') for line in file[0].split('\n'))]
    ids = file[1].split('\n')
    nb_valid = 0

    for id in ids:
        for x, y in ranges.__iter__():
            if x <= int(id) <= y:
                nb_valid += 1
                logging.debug(f"ID {id} is valid for range {(x, y)}")
                break

    logging.info(f"Number of valid IDs: {nb_valid}")

def is_overlapping(range1: range, range2: range):
    return not (range1.stop < range2.start or range2.stop < range1.start)

def update_range(range1: range, range2: range):
    return (min(range1.start, range2.start), max(range1.stop, range2.stop))

def get_overlappings_and_new_range(_range: range, ranges: list[range]):
    overlappings = [r for r in ranges if is_overlapping(_range, r)]
    min_new_start = min([r.start for r in overlappings] + [_range.start])
    max_new_stop = max([r.stop for r in overlappings] + [_range.stop])

    return overlappings, range(min_new_start, max_new_stop)


def solve_part_2(input_file):
    file = open(input_file, "r").read().split("\n\n")

    ranges = [ range(int(x), int(y) + 1) for x, y in (line.split('-') for line in file[0].split('\n'))]

    unonverlapping_ranges = []
    logging.debug(f"Initial ranges: {ranges}")
    for r in ranges:
        logging.debug(f"[1] Processing range: {r}")
        overlappings, new_range = get_overlappings_and_new_range(r, unonverlapping_ranges)
        logging.debug(f"[2] Found overlappings: {overlappings}, new merged range: {new_range}")
        for o in overlappings:
            unonverlapping_ranges.remove(o)
        unonverlapping_ranges.append(new_range)
        logging.debug(f"[3] Updated unoverlapping_ranges: {unonverlapping_ranges}")
    
    logging.debug(f"Unoverlapping ranges: {unonverlapping_ranges}")
    
    total_ids = sum( [ len(r) for r in unonverlapping_ranges ] )
    logging.info(f"Number of unique valid IDs: {total_ids}")



if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    logging.info(f"Elapsed in {1000 * (end - start)} secondes")
