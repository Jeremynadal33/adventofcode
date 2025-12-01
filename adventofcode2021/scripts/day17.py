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
    file = open(input_file, "r").read()
    min_x, max_x, min_y, max_y = read_target(file)

    vxs = [ind for ind in range(750)]
    vys = [ind for ind in range(-700, 750)]
    highs = []
    for vx_init in vxs:
        for vy_init in vys:
            vx = vx_init
            vy = vy_init
            x, y, vx, vy, highiest, hit = shoot(vx, vy, min_x, max_x, min_y, max_y)
            if hit:
                highs.append(highiest)
                # print(x, y, vx_init, vy_init, highiest)

    print("The highest y is : ", max(highs))
    print("Total hit number : ", len(highs))


def solve_part_2(input_file):
    print("Solving puzzle part 2")
    print("can be solved in part 1 ")


def is_on_target(x, y, min_x, max_x, min_y, max_y):
    return min_x <= x <= max_x and min_y <= y <= max_y


def shoot(init_vx, init_vy, min_x, max_x, min_y, max_y):
    x, y = 0, 0
    vx, vy = init_vx, init_vy
    num_steps = 0
    missed = False
    highiest = 0
    while (
        not is_on_target(x, y, min_x, max_x, min_y, max_y)
        and num_steps < 1000
        and not missed
    ):
        x, y, vx, vy = step(x, y, vx, vy)
        num_steps += 1
        if y > highiest:
            highiest = y
        if y < min_y or x > max_x:
            missed = True

    return x, y, vx, vy, highiest, (num_steps < 1000 and not missed)


def step(x, y, vx, vy):
    x += vx
    y += vy
    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1
    vy -= 1

    return x, y, vx, vy


def read_target(input_file):
    for part in input_file.replace(",", "").split(" "):
        if "x" in part:
            part = part.replace("x=", "")
            min_x = part.split("..")[0]
            max_x = part.split("..")[1]
        elif "y" in part:
            part = part.replace("y=", "")
            min_y = part.split("..")[0]
            max_y = part.split("..")[1]
    return int(min_x), int(max_x), int(min_y), int(max_y)


if __name__ == "__main__":
    start = time.time()
    main()
    # print( is_on_target(28, - 7, 20, 30, -10, -5) )
    end = time.time()
    print("Elapsed in {} milisecondes".format(1000 * (end - start)))
