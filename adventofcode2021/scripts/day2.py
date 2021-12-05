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
        solve_part_2(input)

def solve_part_1(input):
    print('Solving puzzle part 1')
    x, y = 0, 0
    file = open(input, 'r').read().split('\n')
    for line in file : 
        x, y = handle_displacement_1(x, y, line)
    print(' After {} displacement, the ship is in {} {}\nMultiplication is {}'.format(len(file),x,y,x*y))

def solve_part_2(input):
    print('Solving puzzle part 2')
    x, y, aim = 0, 0, 0
    file = open(input, 'r').read().split('\n')
    for line in file : 
        x, y , aim = handle_displacement_2(x, y, aim, line)
    print(' After {} displacement, the ship is in {} {}\nMultiplication is {}'.format(len(file),x,y,x*y))


def handle_displacement_1(x, y, line):
    direction = line.split(' ')[0]
    num = int(line.split(' ')[1])

    if direction == 'forward':
        x += num
    elif direction == 'up':
        y -= num
    elif direction == 'down':
        y += num
    else:
        print('ERROR : unknown direction')
    return x, y

def handle_displacement_2(x, y, aim, line):
    direction = line.split(' ')[0]
    num = int(line.split(' ')[1])

    if direction == 'forward':
        x += num
        y += num*aim
    elif direction == 'up':
        aim -= num
    elif direction == 'down':
        aim += num
    else:
        print('ERROR : unknown direction')
    return x, y, aim
     
if __name__ == "__main__":
    main()