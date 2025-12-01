import sys
import numpy as np
import time
from functions import *
import re
import pandas as pd


def main():
    input_file, part = handle_args(sys.argv)
    solve_puzzle(input_file=input_file, part=part)


def solve_puzzle(input_file, part):
    file = open(input_file, "r").read().split("\n\n")
    template = file[0]
    rules = {}
    for line in file[1].split("\n"):
        rules[line.split(" -> ")[0]] = line.split(" -> ")[1]
    if part == 1:
        solve_part_1(template, rules)
    elif part == 2:
        solve_part_2(template, rules)


def solve_part_1(template, rules):
    print("Solving puzzle part 1")

    num_steps = int(input("How many many steps ? \n"))
    print(template)
    for ind in range(num_steps):
        template = step(template, rules)
        # print('step ', ind+1, '\n', template)

    counts = np.unique(list(template), return_counts=True)
    print("Answer : ")
    print(max(counts[1]) - min(counts[1]))


def step(template, rules):
    values_to_append = []
    indexes_to_append = []
    for rule in rules:
        for index in [m.start() for m in re.finditer("(?=" + rule + ")", template)]:
            # We put indexes as they should be in the template at the beginning of the step
            values_to_append.append(rules[rule])
            indexes_to_append.append(index + 1)  # +1 to insert between the two

    to_append = pd.DataFrame()
    to_append["values"] = values_to_append
    to_append["indexes"] = indexes_to_append
    to_append = to_append.sort_values("indexes").reset_index()
    count = 0
    # need to count the number of inserted items to move to the right the others
    for ind in range(to_append.shape[0]):
        value = to_append["values"][ind]
        index = to_append["indexes"][ind]
        template = template[: index + count] + value + template[index + count :]
        count += 1
    return template


def solve_part_2(template, rules):
    print("Solving puzzle part 2")


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed in {} milisecondes".format(1000 * (end - start)))
