
import sys
import numpy as np
import time 
from functions import *

def main():
    input_file, part = handle_args(sys.argv)
    solve_puzzle(input_file = input_file, part = part)

def should_move_tail(xh, yh, xt, yt):
    return not (abs(xh-xt) <= 1 and abs(yh-yt) <= 1)

def move_tail(xh, yh, xt, yt):
    if should_move_tail(xh, yh, xt, yt):
        # if xh - xt == 0: #same column
        #     yt += np.sign(yh - yt) # return either 1 or -1
        # elif yh - yt == 0: #same row
        #     xt += np.sign(xh - xt)
        # print((xh, yh, xt, yt))
        xt += np.sign(xh - xt)
        yt += np.sign(yh - yt)
        # print('deviens')
        # print(xt, yt)
    return xt, yt

def move_head(direction, xh, yh):
    if direction == 'R': return xh +1 , yh
    elif direction == 'L': return xh - 1, yh
    elif direction == 'U': return xh, yh + 1
    elif direction == 'D': return xh, yh - 1
    else: print('unknown direction')

def handle_move(line, xh, yh, xt, yt):
    direction, num = line.split(' ')
    for _ in range(int(num)):
        xh, yh = move_head(direction, xh, yh)
        xt, yt = move_tail(xh, yh, xt, yt)
    return xh, yh, xt, yt

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
    unique_positions = [(0,0)]
    # for xh in range(-2, 2):
    #     for yh in range(-2, 2):
    #         # print(xh, yh, should_move_tail(xh, yh, xt, yt))
    #         move_tail(xh, yh, xt, yt)
    for line in file:
        xh, yh, xt, yt = handle_move(line, xh, yh, xt, yt)
        if (xt, yt) not in unique_positions : unique_positions.append((xt, yt))
        # print(xh, yh)
    print(len(unique_positions))

def solve_part_2(input_file):
    print('Solving puzzle part 2')
    file = open(input_file, 'r').read().split('\n')
    
    
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print('Elapsed in {} milisecondes'.format(1000*(end-start)))