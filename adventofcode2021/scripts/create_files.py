import sys
import os
if __name__ == "__main__":
    prefixes = ['test', 'input']
    parts = ['1', '2']
    try :
        day = int(sys.argv[1])
    except:
        print('ERROR : no day was given or wrong number')

    for prefix in prefixes:
        for part in parts:
            filename = '../inputs/' + prefix + '_day' + str(day) + '_' + part + '.txt'
            if os.path.exists(filename):
                print('File {} already exist'.format(filename))
            else:
                open(filename, "w")
    
    scriptname = 'day' + str(day) + '.py'
    if os.path.exists(scriptname):
        print('File {} already exist'.format(scriptname))
    else:
        f = open(scriptname, "w")
        f.write(
'''
import sys
import numpy as np
import time 
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
    start = time.time()
    file = open(input, 'r').read().split('\\n')

    end = time.time()
    print('Elapsed in {} milisecondes'.format(1000*(end-start)))

def solve_part_2(input):
    print('Solving puzzle part 2')
    start = time.time()
    file = open(input, 'r').read().split('\\n')
    end = time.time()
    print('Elapsed in {} milisecondes'.format(1000*(end-start)))
if __name__ == "__main__":
    main()''')
        f.close()