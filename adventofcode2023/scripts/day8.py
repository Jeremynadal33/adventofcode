import time
from commons.utils import args, logging
import re
import json
import sys
import math

sys.setrecursionlimit(1000000000)
print(sys.getrecursionlimit())

def main():
    file_path = (
        f"adventofcode{args.YEAR}/inputs/input_day{args.DAY}.txt"
        if args.INPUT == "REAL"
        else f"adventofcode{args.YEAR}/inputs/test_day{args.DAY}.txt"
    )
    solve_puzzle(input_file=file_path, part=args.PART)


def solve_puzzle(input_file, part):
    logging.info(f"Solving puzzle part {args.PART}")
    if part == 1:
        solve_part_1(input_file)
    elif part == 2:
        solve_part_2(input_file)

def pprint(_dict):
    print(json.dumps(_dict, indent=2))

def move(source, maps, directions, step):
    if ((args.PART == 1) and source == 'ZZZ') or (args.PART == 2 and source[-1]=='Z'):
        return step
    else:
        next_source = maps[source][directions[step%len(directions)]]
        step += 1
        # print(next_source)
        return move(next_source, maps, directions, step)
    
def move_1_step(source, maps, directions, step):
    next_source = maps[source][directions[step%len(directions)]]
    
    # print(f"source: {source}, direction : {directions[step%len(directions)]}, next : {next_source}" )
    return next_source

def solve_part_1(input_file):
    file = open(input_file, "r").read().split("\n")
    directions = file[0]
    maps = {}

    for line in file[2:]:
        parsed = re.sub(r'[=,()\n]', '', line).replace('  ', ' ').split()
        maps[parsed[0]] = {'L': parsed[1], 'R': parsed[2]}
    print(move('AAA', maps, directions, 0))

def solve_part_2(input_file):
    file = open(input_file, "r").read().split("\n")
    directions = file[0]
    maps = {}

    for line in file[2:]:
        parsed = re.sub(r'[=,()\n]', '', line).replace('  ', ' ').split()
        maps[parsed[0]] = {'L': parsed[1], 'R': parsed[2]}
    
    # sources = []
    # must_continue = True
    # step = 0
    # for map in maps.keys():
    #     if map[-1] == 'A': sources.append(map)
    # while must_continue:
    #     for index in range(len(sources)):
    #         sources[index] = move_1_step(sources[index], maps, directions, step)
    #     all_sources_end = True
    #     for source in sources:
    #         if source[-1] != 'Z': all_sources_end = False
    #     must_continue = not all_sources_end
    #     step += 1
        # print(step, sources)

    # print(step)

    first_ends = []
    for source in maps.keys():
    ## getting segmentation fault after 2... 
        # # if source[-1] == 'A':
        #     tet = move(source, maps, directions, 0)
        #     # print(tet)
        #     first_ends.append(tet)
        #     # !print(source)
        if source[-1] == 'A':
            position = source
            step = 0
            while position[-1] != 'Z':
                # print(position)
                position = move_1_step(position, maps, directions, step)
                step += 1
            first_ends.append(step)
    print(first_ends)
    print(math.lcm(*first_ends))

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    logging.info(f"Elapsed in {1000*(end-start)} secondes")
