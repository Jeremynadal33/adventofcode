import sys
import numpy as np
import time
from functions import *
from functools import reduce


def split_line(line):
    return [int(i) for i in line]


def get_forest(file):
    """dans un premier temps on parse les lignes
    dans un deuxieme temps on transpose le resultat pour avoir les x en premier et y en deuxieme"""
    file = file.split("\n")
    len_y = len(file)
    len_x = len(file[0])
    forest = [split_line(i) for i in file]
    array = np.array(forest)
    transposed_array = array.T
    return transposed_array.tolist(), len_x, len_y


def is_visible(forest, pos_x, pos_y, len_x, len_y):
    """all for loops should change to while visible"""
    height = forest[pos_x][pos_y]
    if pos_x == 0 or pos_x == len_x - 1 or pos_y == 0 or pos_y == len_y - 1:
        return True
    else:
        """check à gauche"""
        visible = True
        for x in range(pos_x):
            # print(x, pos_y, forest[x][pos_y])
            # print('aya')
            if forest[x][pos_y] >= height:
                visible = False
        if visible:
            return visible

        """check à droite"""
        visible = True
        for x in range(pos_x + 1, len_x):
            # print(x, pos_y, forest[x][pos_y])
            # print('aya')
            if forest[x][pos_y] >= height:
                visible = False
        if visible:
            return visible

        """check en haut"""
        visible = True
        for y in range(pos_y):
            if forest[pos_x][y] >= height:
                visible = False
        if visible:
            return visible

        """check en bas"""
        visible = True
        for y in range(pos_y + 1, len_y):
            if forest[pos_x][y] >= height:
                visible = False
        if visible:
            return visible
    return False


def get_nb_visible(forest, pos_x, pos_y, len_x, len_y):
    """all for loops should change to while visible"""
    height = forest[pos_x][pos_y]
    multiplication = []

    """check à gauche"""
    nb_visible = 0
    should_stop = False
    x = pos_x - 1
    while x >= 0 and not should_stop:
        nb_visible += 1
        if forest[x][pos_y] >= height:
            should_stop = True
        x -= 1

    multiplication.append(nb_visible)

    """check à droite"""
    nb_visible = 0
    should_stop = False
    x = pos_x + 1
    while x < len_x and not should_stop:
        nb_visible += 1
        if forest[x][pos_y] >= height:
            should_stop = True
        x += 1

    multiplication.append(nb_visible)

    """check en haut"""
    nb_visible = 0
    should_stop = False
    y = pos_y - 1
    while y >= 0 and not should_stop:
        nb_visible += 1
        if forest[pos_x][y] >= height:
            should_stop = True
        y -= 1

    multiplication.append(nb_visible)
    """check en bas"""
    nb_visible = 0
    should_stop = False
    y = pos_y + 1
    while y < len_y and not should_stop:
        nb_visible += 1
        if forest[pos_x][y] >= height:
            should_stop = True
        y += 1

    multiplication.append(nb_visible)
    # print(multiplication)
    return reduce((lambda x, y: x * y), multiplication)


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
    file = open(input_file, "r").read()

    forest, len_x, len_y = get_forest(file)

    nb_visible = 0
    for x in range(len_x):
        for y in range(len_y):
            print(x, y, is_visible(forest, x, y, len_x, len_y))
            nb_visible += is_visible(forest, x, y, len_x, len_y)

    print(nb_visible)


def solve_part_2(input_file):
    print("Solving puzzle part 2")
    file = open(input_file, "r").read()

    forest, len_x, len_y = get_forest(file)
    visibles = []
    for x in range(len_x):
        for y in range(len_y):
            visibles.append(get_nb_visible(forest, x, y, len_x, len_y))
            # print(x, y, get_nb_visible(forest, x, y, len_x, len_y))
    # print(get_nb_visible(forest, 0, 2, len_x, len_y))
    print(max(visibles))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed in {} milisecondes".format(1000 * (end - start)))
