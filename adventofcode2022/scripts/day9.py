
import sys
import numpy as np
import time 
from functions import *

def main():
    input_file, part = handle_args(sys.argv)
    solve_puzzle(input_file = input_file, part = part)


def move_tail(xh, yh, xt, yt):
    if not (abs(xh-xt) <= 1 and abs(yh-yt) <= 1):
        xt += np.sign(xh - xt)
        yt += np.sign(yh - yt)
    return xt, yt

def move_head(direction, xh, yh):
    if direction == 'R': return xh + 1 , yh
    elif direction == 'L': return xh - 1, yh
    elif direction == 'U': return xh, yh + 1
    elif direction == 'D': return xh, yh - 1
    else: print('unknown direction')

def handle_move(line, xh, yh, xt, yt, unique_positions):
    direction, num = line.split(' ')
    for _ in range(int(num)):
        xh, yh = move_head(direction, xh, yh)
        xt, yt = move_tail(xh, yh, xt, yt)
        if f'{xt}.{yt}' not in unique_positions : unique_positions.append(f'{xt}.{yt}')
        # print(xh, yh, xt, yt)
    return xh, yh, xt, yt, unique_positions


def handle_move_bis(line, knots, unique_positions):
    direction, num = line.split(' ')
    for _ in range(int(num)):
        '''first, we move the head of the rope, then we browse all knots to see if they need to move'''
        knots[0].x, knots[0].y = move_head(direction, knots[0].x, knots[0].y)
        for index in range(1, len(knots)):
            knots[index].x, knots[index].y = move_tail(knots[index - 1].x, knots[index - 1].y, knots[index].x, knots[index].y)
        if knots[-1].str_position() not in unique_positions : unique_positions.append(knots[-1].str_position())
        # print(xh, yh, xt, yt)
    return knots, unique_positions

def solve_puzzle(input_file, part):
    if part == 1 :
        solve_part_1(input_file)
    elif part == 2 :
        solve_part_2(input_file)

def solve_part_1(input_file):
    print('Solving puzzle part 1')
    file = open(input_file, 'r').read().split('\n')
    xh, yh = 0, 0
    xt, yt = 0, 0
    unique_positions = ['0.0']
    # for xh in range(-2, 2):
    #     for yh in range(-2, 2):
    #         # print(xh, yh, should_move_tail(xh, yh, xt, yt))
    #         move_tail(xh, yh, xt, yt)
    for line in file:
        # print(f'------------------{line}-----------------')
        xh, yh, xt, yt, unique_positions = handle_move(line, xh, yh, xt, yt, unique_positions)
        # print(xh, yh)
    print(len(unique_positions))

def solve_part_2(input_file):
    print('Solving puzzle part 2')
    file = open(input_file, 'r').read().split('\n')
    '''instead of only two points, the rope is composed of several points and every point has x and y position
    at position 0 we have the head and at position len_rope - 1 we have the tail'''
    len_rope = 10
    
    knots = [Knot(0, 0, index) for index in range(len_rope)]

    unique_positions = ['0.0']
    for line in file:
        print(f'------------------{line}-----------------')
        knots, unique_positions = handle_move_bis(line, knots, unique_positions)
        for knot in knots : knot.describe()
    print(len(unique_positions))

class Knot:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index
    def describe(self):
        print(f"knot {self.index} : x = {self.x} ; y = {self.y}")
    def str_position(self):
        return f"{self.x}.{self.y}"

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print('Elapsed in {} milisecondes'.format(1000*(end-start)))
    # test = Knot(0, 0)
    # test.x = 1
    # test.describe()
    # print(test.str_position())