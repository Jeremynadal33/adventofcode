import sys
import time
from functions import *


def main():
    input_file, part = handle_args(sys.argv)
    solve_puzzle(input_file=input_file, part=part)


def solve_puzzle(input_file, part):
    if part == 1:
        solve_part_1(input_file)
    elif part == 2:
        solve_part_2(input_file)


def solve_part_1(input_file):
    print("Solving puzzle part 1")
    # file = file.replace(',', ', ')
    input_array = open(input_file).read().strip().split("\n")
    input_array = list(input_array)
    print(input_array)


def solve_part_2(input_file):
    print("Solving puzzle part 2")
    open(input_file, "r").read().split("\n")


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed in {} milisecondes".format(1000 * (end - start)))
