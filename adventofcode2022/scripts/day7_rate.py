import sys
import numpy as np
import time
from functions import *


def handle_line(item, file_system, current_path):
    if item[0] == "$":
        current_path = handle_command(item, current_path)
    else:
        file_system = put_item(item, file_system, current_path)

    return file_system, current_path


def handle_command(item, current_path):
    command = item.split(" ")[1:]
    if command[0] == "ls":
        return current_path
    elif command[0] == "cd":
        if command[1] == ".." and current_path[-1] != "/":
            return current_path[:-1]
        elif command[1] == "..":
            return current_path
        else:
            current_path.append(command[1] + "/")
            return current_path
    else:
        print("unknown command")


def put_item(item, file_system, current_path):
    command = item.split(" ")

    if command[0] == "dir":
        pass
    else:
        file_system["".join(current_path) + command[1] + str(time.time())] = int(
            command[0]
        )
    return file_system


def get_unique_directories(file_system):
    dirs = np.unique(["/".join(file.split("/")[:-1]) for file in file_system.keys()])
    dirs[0] = "/"
    return dirs


def get_size_per_directory(directories, file_system):
    sizes = [0 for _ in directories]
    for index in range(len(directories)):
        for file, size in file_system.items():
            if directories[index] in file:
                sizes[index] += size
    return sizes


def get_sum_sizes(sizes, threshold):
    return sum([size for size in sizes if size <= threshold])


def main():
    input_file, part = handle_args(sys.argv)
    solve_puzzle(input_file=input_file, part=part)


def solve_puzzle(input_file, part):
    if part == 1:
        solve_part_1(input_file)
    elif part == 2:
        solve_part_2(input_file)


def solve_part_1(input_file):
    """we represent the whole file system in a dict
    current_path is pwd
    """
    print("Solving puzzle part 1")
    file = open(input_file, "r").read().split("\n")
    file_system = {}
    current_path = ["/"]  # first instruction is cd / to go to root
    threshold = 100000

    for item in file[1:]:
        file_system, current_path = handle_line(item, file_system, current_path)

    """now we have a dictionary of all files with their path, we should regroup every item in the same dir"""
    directories = get_unique_directories(file_system)
    sizes = get_size_per_directory(directories, file_system)

    print(get_sum_sizes(sizes, threshold))
    # for index in range(len(directories)):
    #     print(directories[index], sizes[index] )
    # print(directories)
    # print(sizes)
    # print(file_system)
    # wrong : 1402403


def solve_part_2(input_file):
    print("Solving puzzle part 2")
    file = open(input_file, "r").read().split("\n")
    new = open("cleaned.txt", "w")
    for line in file:
        if line[:3] != "dir":
            new.write(line + "\n")


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed in {} milisecondes".format(1000 * (end - start)))
