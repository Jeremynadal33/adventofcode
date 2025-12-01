import sys
import time
from functions import *
from collections import defaultdict

"""
we store in sizes the path of a dir and the size of its direct files
in children, a list of the dirs inside him
"""


def handle_cd(block, current_path):
    command = block.split(" ")
    if command[1] == ".." and current_path[-1] != "/":
        return current_path[:-1]
    elif command[1] == "..":
        return current_path
    else:
        current_path.append(command[1] + "/")
        return current_path


def get_command_blocks(file):
    """split in commands and their output the first command is cd /"""
    return file.split("\n$ ")[1:]


def handle_block(block, current_path, sizes, children):
    if block.split(" ")[0] == "cd":
        current_path = handle_cd(block, current_path)
        # print(current_path)
    elif block.split("\n")[0] == "ls":
        size, children = handle_ls(block.split("\n")[1:], current_path, children)
        sizes["".join(current_path)] = size
        # print(block.split('\n')[1:])
    return current_path, sizes, children


def handle_ls(block, current_path, children):
    size = 0
    for line in block:
        parts = line.split(" ")
        if parts[0] == "dir":
            children["".join(current_path)].append(
                "".join(current_path) + str(parts[1])
            )
        else:
            size += int(parts[0])
    return size, children


def dfs(abspath, sizes, children):
    size = sizes[abspath]
    for child in children[abspath]:
        size += dfs(child, sizes, children)
    return size


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

    current_path = ["/"]
    sizes = defaultdict(int)
    children = defaultdict(list)

    blocks = get_command_blocks(file)
    for block in blocks:
        # print(block)
        # print('---------')
        current_path, sizes, children = handle_block(
            block, current_path, sizes, children
        )

    print(sizes.items())
    print(children.items())
    sum = 0
    for index in range(len(sizes)):
        # print(list(sizes.keys())[index], dfs(list(sizes.keys())[index], sizes, children))
        size = dfs(list(sizes.keys())[index], sizes, children)
        if size < 100000:
            sum += size
    print(sum)
    # 1642445 too low


def solve_part_2(input_file):
    print("Solving puzzle part 2")
    open(input_file, "r").read().split("\n")


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed in {} milisecondes".format(1000 * (end - start)))
