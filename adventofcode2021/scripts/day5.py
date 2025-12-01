import sys
import numpy as np
from functions import *


def main():
    input_txt, part = handle_args(sys.argv)
    solve_puzzle(input=input_txt, part=part)


def solve_puzzle(input, part):
    file = open(input, "r").read().split("\n")
    # retrive all coordinates to create a matrix
    x1s, y1s, x2s, y2s = handle_file(file)
    # we make a matrix of zeros with size max(x2s,y2s)
    max_x = max(max(x1s), max(x2s))
    max_y = max(max(y1s), max(y2s))
    matrix = np.zeros((max_x + 1, max_y + 1))  # shape must include 0 and max_x/y

    if part == 1:
        solve_part_1(matrix, x1s, y1s, x2s, y2s)
    elif part == 2:
        solve_part_2(matrix, x1s, y1s, x2s, y2s)


def solve_part_1(matrix, x1s, y1s, x2s, y2s):
    print("Solving puzzle part 1")

    for index in range(len(x1s)):
        matrix = add_hor_vert_line(
            matrix, x1s[index], y1s[index], x2s[index], y2s[index]
        )

    xs, ys = np.where(matrix > 1)
    print(
        "There are {} points of at least 2 overlapping vertical/horizontal lines".format(
            xs.shape[0]
        )
    )


def add_hor_vert_line(matrix, x1, y1, x2, y2):
    # if part = 1 then only add vertical and horizontal lines
    if x1 == x2:
        # draw vertical line
        for index in range(min(y1, y2), max(y1, y2) + 1):
            matrix[x1, index] += 1
    elif y1 == y2:
        # draw horizontal line
        for index in range(min(x1, x2), max(x1, x2) + 1):
            matrix[index, y1] += 1
    return matrix


def handle_file(file):
    x1s, y1s, x2s, y2s = [], [], [], []
    for line in file:
        x1, y1, x2, y2 = handle_line(line)
        x1s.append(x1), y1s.append(y1), x2s.append(x2), y2s.append(y2)
    return x1s, y1s, x2s, y2s


def handle_line(line):
    # returns x1, y1, x2, y2
    x1, y1 = line.split(" -> ")[0].split(",")
    x2, y2 = line.split(" -> ")[1].split(",")
    return int(x1), int(y1), int(x2), int(y2)


def add_line(matrix, x1, y1, x2, y2):
    # print('---------------')
    # print(x1, y1, x2, y2)

    # if part = 1 then only add vertical and horizontal lines
    if x1 == x2:
        # draw vertical line
        for index in range(min(y1, y2), max(y1, y2) + 1):
            matrix[x1, index] += 1
    elif y1 == y2:
        # draw horizontal line
        for index in range(min(x1, x2), max(x1, x2) + 1):
            matrix[index, y1] += 1
    else:
        if x1 > x2:
            xs = [i for i in range(x1, x2 - 1, -1)]
        else:
            xs = [i for i in range(x1, x2 + 1)]
        if y1 > y2:
            ys = [i for i in range(y1, y2 - 1, -1)]
        else:
            ys = [i for i in range(y1, y2 + 1)]
        # print(xs)
        # print(ys)
        for index in range(len(xs)):
            matrix[xs[index], ys[index]] += 1
    # print(matrix)
    # print('---------------')
    return matrix


def solve_part_2(matrix, x1s, y1s, x2s, y2s):
    print("Solving puzzle part 2")

    for index in range(len(x1s)):
        matrix = add_line(matrix, x1s[index], y1s[index], x2s[index], y2s[index])
    # index = 1
    # add_line(matrix, x1s[index], y1s[index], x2s[index], y2s[index])
    xs, ys = np.where(matrix > 1)
    print(
        "There are {} points of at least 2 overlapping vertical/horizontal lines".format(
            xs.shape[0]
        )
    )


if __name__ == "__main__":
    main()
