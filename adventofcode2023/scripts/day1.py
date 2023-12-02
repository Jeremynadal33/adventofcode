import re
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
    logging.info(f"Solving puzzle part {args.PART}")
    if part == 1:
        solve_part_1(input_file)
    elif part == 2:
        solve_part_2(input_file)


def solve_part_1(input_file):
    file = open(input_file, "r").read().split("\n")
    sum = 0
    for line in file:
        nums = re.sub("[a-z]", "", line)
        sum += int(f"{nums[0]}{nums[-1]}")

    logging.info(sum)


def solve_part_2(input_file):
    file = open(input_file, "r").read().split("\n")
    num_letters = {
        8: "eight",
        7: "seven",
        3: "three",
        1: "one",
        2: "two",
        4: "four",
        5: "five",
        6: "six",
        9: "nine",
    }
    sum = 0
    for line in file:
        nums = ""
        for i in range(0, len(line)):
            sub_line = line[i:i+5]  # We can look at only 5 since
            for key, value in num_letters.items():
                if sub_line.startswith(value):
                    nums += str(key)
                if sub_line[0] == str(key):
                    nums += str(key)
        sum += int(f"{nums[0]}{nums[-1]}")

    logging.info(sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    logging.info(f"Elapsed in {1000*(end-start)} secondes")
