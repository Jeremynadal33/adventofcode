
import sys
import numpy as np
import time 
from functions import *


def char_to_priority(char):
    if char.isupper():
        return 26 + ord(char) - 64
    else:
        return ord(char) - 96

def get_redundant_char(line, part = 1):
    if part == 1:
        '''the line contains both compartment (same size) '''
        compartment_length = int(len(line)/2)
        
        chars_first = np.unique(list(line[:compartment_length]))
        chars_second = np.unique(list(line[compartment_length:]))
        return [item for item in chars_first if item in chars_second]
    else:
        '''in part 2, line is actualy a list of the all the ruckstack of the elves in a group'''
        result = set(line[0])
        for item in line[1:]:
            result = result.intersection(set(item))
        return list(result)

def main():
    input_file, part = handle_args(sys.argv)
    solve_puzzle(input_file = input_file, part = part)

def solve_puzzle(input_file, part):
    if part == 1 :
        solve_part_1(input_file)
    elif part == 2 :
        solve_part_2(input_file)

def solve_part_1(input_file):
    print('Solving puzzle part 1')
    file = open(input_file, 'r').read().split('\n')

    summ = 0
    for item in file:
        summ += sum([char_to_priority(char) for char in get_redundant_char(item)])

    print( summ )


def solve_part_2(input_file):
    print('Solving puzzle part 2')
    file = open(input_file, 'r').read().split('\n')

    nb_elves_in_group = 3
    num_line = 0
    summ = 0
    while num_line + nb_elves_in_group <= len(file):
        summ += sum([char_to_priority(char) for char in get_redundant_char(file[num_line : num_line + nb_elves_in_group], part = 2)])

        num_line += nb_elves_in_group
    print( summ )
    
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print('Elapsed in {} milisecondes'.format(1000*(end-start)))