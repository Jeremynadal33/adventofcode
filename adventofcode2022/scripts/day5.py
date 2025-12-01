import sys
import time
from functions import *


def build_stacks(drawing):
    """On the drawing, the last line is useless.
    The last line gives us the number of stacks and the ith crate is at the
    We want to build the stack from the end.
    We try to access the corresponding stack, if it fails that means the stack doesnt exist yet
    (on the first append) so we create it"""
    stacks = []
    nb_stacks = max([int(i) for i in drawing[-1].split(" ") if i != ""])

    for line in drawing[::-1][1:]:
        for nb_stack in range(nb_stacks):
            crate = line[4 * nb_stack + 1]
            if crate != " ":
                try:
                    stacks[nb_stack].append(crate)
                except:
                    stacks.append([crate])
    return stacks


def handle_instruction(stacks, line):
    splitted_line = line.split(" ")
    nb_to_move = int(splitted_line[1])
    to_move_from = int(splitted_line[3]) - 1  # index of stack 1 is 0
    to_move_to = int(splitted_line[5]) - 1

    for _ in range(nb_to_move):
        stacks[to_move_to].append(stacks[to_move_from].pop())
    return stacks


def handle_instruction_9001(stacks, line):
    splitted_line = line.split(" ")
    nb_to_move = int(splitted_line[1])
    to_move_from = int(splitted_line[3]) - 1  # index of stack 1 is 0
    to_move_to = int(splitted_line[5]) - 1

    stacks[to_move_to].extend(stacks[to_move_from][-nb_to_move:])
    for _ in range(nb_to_move):
        stacks[to_move_from].pop()
    return stacks


def display_top_stacks(stacks):
    return "".join([stack[-1] for stack in stacks])


def main():
    input_file, part = handle_args(sys.argv)
    solve_puzzle(input_file=input_file, part=part)


def solve_puzzle(input_file, part):
    if part == 1:
        solve_part_1(input_file)
    elif part == 2:
        solve_part_2(input_file)


def solve_part_1(input_file):
    """We will handle a list of stacks (deque in our case)
    1. We begin by separating inital stacks from instructions
    2. Method that builds the stacks
    3. Method that handle instructions from a line"""

    print("Solving puzzle part 1")
    file = open(input_file, "r").read().split("\n\n")
    drawing = file[0].split("\n")
    instructions = file[1].split("\n")

    stacks = build_stacks(drawing)

    for instruction in instructions:
        # print(instruction)
        stacks = handle_instruction(stacks, instruction)

    print(stacks)
    print(display_top_stacks(stacks))


def solve_part_2(input_file):
    print("Solving puzzle part 2")
    file = open(input_file, "r").read().split("\n\n")
    drawing = file[0].split("\n")
    instructions = file[1].split("\n")

    stacks = build_stacks(drawing)

    for instruction in instructions:
        # print(instruction)
        stacks = handle_instruction_9001(stacks, instruction)

    print(stacks)
    print(display_top_stacks(stacks))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed in {} milisecondes".format(1000 * (end - start)))
