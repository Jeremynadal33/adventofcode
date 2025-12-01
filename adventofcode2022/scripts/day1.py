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
    file = open(input_file, "r").read().split("\n")
    print(file)
    sums = [0]
    for item in file:
        if item != "":
            sums[-1] += int(item)
        else:
            sums.append(0)
    print(max(sums))

    top = 3
    sum = 0
    for _ in range(top):
        index = sums.index(max(sums))
        sum += sums.pop(index)
    print(sum)


def solve_part_2(input_file):
    print("Solving puzzle part 2")
    open(input_file, "r").read().split("\n")


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed in {} milisecondes".format(1000 * (end - start)))
