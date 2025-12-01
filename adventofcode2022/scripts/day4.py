import sys
import time
from functions import *


def handle_line(line):
    """should return one range for each elf in the pair
    maybe it would be more efficient just to keep min and max but just in case we need it for part 2"""
    elf_1 = range(
        int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1
    )
    elf_2 = range(
        int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]) + 1
    )
    return elf_1, elf_2


def is_pairs_fully_overlap(elf_1, elf_2):
    """return boolean if one of the pairs is fully contained into the other"""
    return (elf_1[0] in elf_2 and elf_1[-1] in elf_2) or (
        elf_2[0] in elf_1 and elf_2[-1] in elf_1
    )


def is_pairs_overlap(elf_1, elf_2):
    """return boolean if one of the pairs overlaps the other
    two situations:
        * max of 1 is smaller than min of 2
        * min of 1 is greater than max of 2"""
    # print(elf_1, elf_2)
    # print( elf_1[-1] < elf_2[0] or elf_1[0] > elf_2[-1] )
    # print( elf_2[-1] < elf_1[0] or elf_2[0] > elf_1[-1] )
    # print('---------')
    return not (
        elf_1[-1] < elf_2[0] or elf_1[0] > elf_2[-1]
    )  # and (elf_2[-1] <= elf_1[0] or elf_2[0] >= elf_1[-1]) )


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

    summ = 0
    for line in file:
        summ += is_pairs_fully_overlap(*handle_line(line))

    print(summ)


def solve_part_2(input_file):
    print("Solving puzzle part 2")
    file = open(input_file, "r").read().split("\n")

    summ = 0
    for line in file:
        summ += is_pairs_overlap(*handle_line(line))
        print(is_pairs_overlap(*handle_line(line)))

    print(summ)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed in {} milisecondes".format(1000 * (end - start)))
