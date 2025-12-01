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


def should_store_register(cycle):
    return (cycle - 20) % 40 == 0


def should_go_to_line(cycle):
    return (cycle - 1) % 40 == 0


def draw_pixel(X, cycle):
    if cycle == 40 and X in [39, 40, 41]:
        retu = "#"
    elif abs(cycle % 40 - X) <= 1 and cycle != 40:
        retu = "#"
    else:
        retu = "."
    print(f"draw x: {X}, cycle: {cycle} => {retu}")
    return retu


def get_sum_signal_strength(signals):
    sum = 0
    for index in range(len(signals)):
        sum += (20 + 40 * index) * signals[index]
    return sum


def solve_part_1(input_file):
    print("Solving puzzle part 1")
    file = open(input_file, "r").read().split("\n")
    """lets gather all interesting of the register, the first is at 20th cycle and then every 40"""
    interesting = []
    cycle_count = 1  # on commence à 1 -> première instruction est dans le premier cycle
    X = 1
    for line in file:
        intructions = line.split(" ")
        if should_store_register(cycle_count):
            interesting.append(X)
        if len(intructions) == 1:
            cycle_count += 1
        else:
            """on refait un tour"""
            cycle_count += 1
            if should_store_register(cycle_count):
                interesting.append(X)
            cycle_count += 1
            X += int(intructions[-1])

    print(get_sum_signal_strength(interesting))


def solve_part_2(input_file):
    print("Solving puzzle part 2")
    file = open(input_file, "r").read().split("\n")
    output = open("../outputs/output_10.txt", "w")
    cycle_count = 1  # on commence à 1 -> première instruction est dans le premier cycle
    X = 1
    for line in file:
        intructions = line.split(" ")

        if len(intructions) == 1:
            if should_go_to_line(cycle_count):
                output.write("\n")
            output.write(draw_pixel(X, cycle_count - 1))
            # output.write(f"{cycle_count}")
            cycle_count += 1
        else:
            if should_go_to_line(cycle_count):
                output.write("\n")
            output.write(draw_pixel(X, cycle_count - 1))
            # output.write(f"{cycle_count}")
            cycle_count += 1
            if should_go_to_line(cycle_count):
                output.write("\n")
            output.write(draw_pixel(X, cycle_count - 1))
            # output.write(f"{cycle_count}")
            cycle_count += 1
            X += int(intructions[-1])
        print(cycle_count, X)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed in {} milisecondes".format(1000 * (end - start)))
