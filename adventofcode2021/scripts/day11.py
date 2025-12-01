import sys
import numpy as np
import time
from functions import *


def main():
    input_txt, part = handle_args(sys.argv)
    solve_puzzle(input=input_txt, part=part)


def solve_puzzle(input, part):
    matrix = np.genfromtxt(input, delimiter=1, dtype=int)
    if part == 1:
        solve_part_1(matrix)
    elif part == 2:
        solve_part_2()


def solve_part_1(matrix):
    print("Solving puzzle part 1")
    num_flashs = 0
    print("INIT")
    print(matrix)
    max_steps = int(input("How many steps should we do ? \n"))
    for count in range(max_steps):
        matrix, num_flashs = step(matrix, num_flashs)
        if np.where(matrix == 1)[0].shape[0] == matrix.shape[0] * matrix.shape[1]:
            print("All octopuses flashed at step : ", count)
    print(
        "After {} steps, there was a total of {} flashs".format(max_steps, num_flashs)
    )


def step(matrix, num_flashs):
    flashed = np.zeros((matrix.shape[0], matrix.shape[1]))
    matrix += 1

    while np.where(matrix > 9)[0].shape[0] > 0:
        xs = np.where(matrix > 9)[0]
        ys = np.where(matrix > 9)[1]

        for ind in range(xs.shape[0]):
            # each location can only flash once
            if flashed[xs[ind], ys[ind]] == 0:
                flashed[xs[ind], ys[ind]] += 1
                matrix[xs[ind], ys[ind]] = 0
                adjacents = find_adjacents(matrix, xs[ind], ys[ind])
                for adj in range(len(adjacents)):
                    matrix[adjacents[adj][0], adjacents[adj][1]] += 1

    # put every flashed position to 0
    xs = np.where(flashed == 1)[0]
    ys = np.where(flashed == 1)[1]
    for ind in range(xs.shape[0]):
        matrix[xs[ind], ys[ind]] = 0
    # print('there was {} flashs'.format(np.sum(flashed)))
    return matrix, num_flashs + np.sum(flashed)


def find_adjacents(matrix, x, y):
    adjacents = []
    # check if we are at the left border :
    if x == 0:
        # check if we are at the top
        if y == 0:
            adjacents.extend([(x + 1, y), (x, y + 1), (x + 1, y + 1)])
        # check if we are at the bottom
        elif y == matrix.shape[1] - 1:
            adjacents.extend([(x + 1, y), (x, y - 1), (x + 1, y - 1)])
        else:
            adjacents.extend(
                [(x + 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x + 1, y - 1)]
            )
    # check if we are on the right border
    elif x == matrix.shape[0] - 1:
        # check if we are at the top
        if y == 0:
            adjacents.extend([(x - 1, y), (x, y + 1), (x - 1, y + 1)])
        # check if we are at the bottom
        elif y == matrix.shape[1] - 1:
            adjacents.extend([(x - 1, y), (x, y - 1), (x - 1, y - 1)])
        else:
            # on the right but not corner
            adjacents.extend(
                [(x - 1, y), (x - 1, y - 1), (x, y - 1), (x - 1, y + 1), (x, y + 1)]
            )
    # else we are not in a border
    else:
        # check if we are at the top
        if y == 0:
            adjacents.extend(
                [(x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y)]
            )
        # check if we are at the bottom
        elif y == matrix.shape[1] - 1:
            adjacents.extend(
                [(x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y)]
            )
        else:
            # in the middle so search everywhere
            adjacents.extend(
                [
                    (x - 1, y - 1),
                    (x, y - 1),
                    (x + 1, y - 1),
                    (x - 1, y),
                    (x + 1, y),
                    (x - 1, y + 1),
                    (x, y + 1),
                    (x + 1, y + 1),
                ]
            )
    return adjacents


def solve_part_2():
    print("Solving puzzle part 2")
    print("Part 2 can be solved inside part 1")


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed in {} milisecondes".format(1000 * (end - start)))
