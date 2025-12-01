import sys
import time
from functions import *


def get_marker_start(datastream, nb_unique_to_check=4):
    for index in range(len(datastream) - nb_unique_to_check):
        if (
            len(set(datastream[index : index + nb_unique_to_check]))
            == nb_unique_to_check
        ):
            return index + nb_unique_to_check
    return -1


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
    file = open(input_file, "r").read().split("\n")

    for datastream in file:
        print(get_marker_start(datastream))


def solve_part_2(input_file):
    print("Solving puzzle part 2")
    file = open(input_file, "r").read().split("\n")

    for datastream in file:
        print(get_marker_start(datastream, nb_unique_to_check=14))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed in {} milisecondes".format(1000 * (end - start)))
