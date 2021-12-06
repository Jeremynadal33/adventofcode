
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

def solve_part_1(input_txt):
    print('Solving puzzle part 1')
    init = open(input_txt, 'r').read().split(',')
    init = [ int(i) for i in init]
    iterations = int(input('Enter number of days wanted: '))

    for _ in range(iterations):
        to_append = []
        for ind in range(len(init)):
            if init[ind] == 0:
                to_append.append(8) #new spawn
                init[ind] = 6       #reinit count down
            else : 
                init[ind] -= 1
        init.extend(to_append)
    print('After {} days, there are {} fishs'.format(iterations, len(init)))
    


def solve_part_2(input):
    print('Solving puzzle part 2')
    file = open(input, 'r').read().split('\n')
    
if __name__ == "__main__":
    main()
    # username = input("Enter username:")
    # print("Username is: " + username)