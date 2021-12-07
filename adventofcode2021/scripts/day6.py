
import sys
import numpy as np
from functions import *
import time 

def main():
    input_txt, part = handle_args(sys.argv)
    solve_puzzle(input = input_txt, part = part)

def solve_puzzle(input, part):
    if part == 1 :
        solve_part_1(input)
    elif part == 2 :
        solve_part_2(input)

def solve_part_1(input_txt):
    print('Solving puzzle part 1')
    iterations = int(input('Enter number of days wanted: '))
    start = time.time()
    init = open(input_txt, 'r').read().split(',')
    init = [ int(i) for i in init]

    # for _ in range(iterations):
    #     to_append = []
    #     for ind in range(len(init)):
    #         if init[ind] == 0:
    #             to_append.append(8) #new spawn
    #             init[ind] = 6       #reinit count down
    #         else : 
    #             init[ind] -= 1
    #     init.extend(to_append)
    # print('After {} days, there are {} fishs'.format(iterations, len(init)))
    
    # better idea : lets make a vector with indice from 0 to 8 corresponding to its life
    # and count the number of fish in each state
    
    fishs = [0 for _ in range(9)]
    for i in init:
        fishs[i] += 1
    for _ in range(iterations):
        new = fishs.pop(0)
        fishs.append(new)
        fishs[6] += new
    end = time.time()
    print('After {} days, there are {} fishs'.format(iterations, sum(fishs)))
    print('Elapsed in {} milisecondes'.format(1000*(end-start)))


def solve_part_2(input):
    print('Solving puzzle part 2')
    print('This puzzle solves both parts using 1.')

if __name__ == "__main__":
    main()
    # username = input("Enter username:")
    # print("Username is: " + username)
    # test = [i for i in range(9) ]
    # print(test)
    # print(test.pop(0))
    # print(test)