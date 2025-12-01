import sys
import numpy as np
import time
from functions import *


def main():
    input_txt, part = handle_args(sys.argv)
    solve_puzzle(input=input_txt, part=part)


def solve_puzzle(input, part):
    locations = open(input, "r").read().split("\n\n")[0].split("\n")
    folds = open(input, "r").read().split("\n\n")[1].split("\n")

    xs = []
    ys = []
    fold_dir = []
    fold_num = []
    for line in locations:
        xs.append(int(line.split(",")[0]))
        ys.append(int(line.split(",")[1]))

    for line in folds:
        fold_dir.append(line.split(" ")[-1].split("=")[0])
        fold_num.append(int(line.split(" ")[-1].split("=")[1]))
    if part == 1:
        solve_part_1(xs, ys, fold_dir, fold_num)
    elif part == 2:
        solve_part_2(xs, ys, fold_dir, fold_num)


def solve_part_1(xs, ys, fold_dir, fold_num):
    print("Solving puzzle part 1")

    matrix = np.zeros((max(ys) + 1, max(xs) + 1))
    for ind in range(len(xs)):
        matrix[ys[ind], xs[ind]] += 1

    print(matrix)
    for ind in range(len(fold_dir)):
        print(
            "Fold in the {} direction, at number {}".format(
                fold_dir[ind], fold_num[ind]
            )
        )
        matrix = fold(matrix, fold_dir[ind], fold_num[ind])
        print(matrix)
        print(visible_dots(matrix))

    f = open("day13.out", "w")
    for y in range(matrix.shape[0]):
        for x in range(matrix.shape[1]):
            if matrix[y, x] == 0:
                f.write(" ")
            else:
                f.write("#")
        f.write("\n")

    f.close()


def fold(matrix, dir, num):
    if dir == "x":
        assert num < matrix.shape[1], "Fold on axis x is outter bound"
        new_matrix = matrix[:, :num]
        old = matrix[:, num:]
        for x in range(old.shape[1]):
            for y in range(matrix.shape[0]):
                new_matrix[y, -x] += old[y, x]
        return new_matrix
    elif dir == "y":
        assert num < matrix.shape[0], "Fold on axis y is outter bound"
        new_matrix = matrix[:num, :]
        old = matrix[num:, :]
        for y in range(old.shape[0]):
            for x in range(matrix.shape[1]):
                new_matrix[-y, x] += old[y, x]
        return new_matrix
    else:
        print("Unknown direction")


def solve_part_2(xs, ys, fold_dir, fold_num):
    print("Solving puzzle part 2")
    print("Can be solved in part 1")


def visible_dots(matrix):
    return np.where(matrix > 0)[0].shape[0]


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed in {} milisecondes".format(1000 * (end - start)))
