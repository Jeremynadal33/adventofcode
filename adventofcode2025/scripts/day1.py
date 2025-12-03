import time
from commons.utils import args, logging

global dial_position 
dial_position = 50


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
    file = open(input_file, "r").read().split("\n")
    count = 0
    global dial_position
    for f in file:
        direction = 1 if f[0] == "R" else -1
        steps = int(f[1:])
        dial_position += direction * steps
        dial_position = dial_position % 100
        logging.debug(f"Move {f}: dial position is {dial_position}")
        if dial_position == 0:
            count += 1
    logging.info(f"Dial went {count} times on the 0 position")


def solve_part_2(input_file):
    file = open(input_file, "r").read().split("\n")
    dial_0_count = 0
    global dial_position
    for f in file:
        direction = 1 if f[0] == "R" else -1
        steps = int(f[1:])
        nb_complete_rounds = steps // 100
        rest_steps = steps % 100
        tmp_position = dial_position + direction * rest_steps

        dial_0_count += nb_complete_rounds
        if nb_complete_rounds > 0:
            logging.debug(
                f"Dial made {nb_complete_rounds} complete rounds during move {f}"
            )
        
        # if we start at 0, we should not count it
        if dial_position != 0 and (tmp_position >= 100 or tmp_position <= 0):
            logging.debug(f"Dial crossed or finished on 0 position during move {f}")
            dial_0_count += 1

        logging.debug(f"Move {f}: dial position is {dial_position}")
        dial_position = tmp_position % 100

    logging.info(f"Dial passed {dial_0_count} times on the 0 position")


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    logging.info(f"Elapsed in {1000 * (end - start)} secondes")
