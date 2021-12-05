import sys
import numpy as np
from functions import *

def main():
    input_txt, part = handle_args(sys.argv)
    solve_puzzle(input = input_txt, part = part)

def solve_puzzle(input, part):
    if part == 1 :
        solve_part_1(input)
    elif part == 2 :
        print(input)
        solve_part_2(input)

def solve_part_1(input):
    print('Solving puzzle part 1')

    file = open(input, 'r').read().split('\n')
    

def solve_part_2(input):
    print('Solving puzzle part 2')

    file = open(input, 'r').read().split('\n')
    for index in range(len(file)):
        file[index] = int(file[index].split(' ')[0])
    print(file)


if __name__ == "__main__":
    main()