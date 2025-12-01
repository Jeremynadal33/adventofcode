import sys
import numpy as np
from functions import *


def main():
    input_txt, part = handle_args(sys.argv)
    solve_puzzle(input=input_txt, part=part)


def solve_puzzle(input, part):
    if part == 1:
        solve_part_1(input)
    elif part == 2:
        solve_part_2(input)


def solve_part_1(input):
    print("Solving puzzle part 1")

    file = open(input, "r").read().split("\n")
    count = 0
    prev = file[0]
    for index in range(1, len(file)):
        if prev < file[index]:
            count += 1
        prev = file[index]
    print(count)


def solve_part_2(input):
    print("Solving puzzle part 2")

    file = open(input, "r").read().split("\n")
    for index in range(len(file)):
        file[index] = int(file[index].split(" ")[0])

    # Using concolution as a 1D CNN would do
    convolved_file = np.convolve(file, np.ones(3, dtype=int), "valid")

    count = 0
    prev = convolved_file[0]
    for index in range(1, len(convolved_file)):
        if prev < convolved_file[index]:
            count += 1
        prev = convolved_file[index]
    print(count)


if __name__ == "__main__":
    main()
