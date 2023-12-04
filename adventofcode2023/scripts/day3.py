import time
from commons.utils import args, logging
import re
import numpy as np

def main():
    file_path = f"adventofcode{args.YEAR}/inputs/input_day{args.DAY}.txt" if args.INPUT == "REAL" else f"adventofcode{args.YEAR}/inputs/test_day{args.DAY}.txt" 
    solve_puzzle(input_file = file_path, part = args.PART)

def solve_puzzle(input_file, part):
    logging.info(f"Solving puzzle part {args.PART}")
    if part == 1 :
        solve_part_1(input_file)
    elif part == 2 :
        solve_part_2(input_file)


def is_touching_symbol(matrix, x, y, symbols):
    '''
        Is char at position x, y in matrix is touching
        a symbol
    '''
    for i in range(max(x-1, 0), min(x+2, len(matrix))):
        for j in range(max(y-1, 0), min(y+2, len(matrix[0]))):

            if matrix[i][j] in symbols:
                return True
    return False

def pos_touching_gear(matrix, x, y):
    '''
        If char at position x, y in matrix is touching
        a * symbol, returns its position
    '''
    for i in range(max(x-1, 0), min(x+2, len(matrix))):
        for j in range(max(y-1, 0), min(y+2, len(matrix[0]))):
            if matrix[i][j] == '*':
                return (i, j)
    return ()

def solve_part_1(input_file):
    file = open(input_file, 'r').read()
    symbols = set(re.sub("[0-9]+|\s|\.", "", file).strip())
    matrix = [list(line) for line in file.split('\n')]
    
    summ = 0

    for x in range(len(matrix)):
        # looking for a number in the line
        curr_num = ""
        y = 0
        while y < len(matrix[0]):
            '''
                lookgin for a digit. Need to reset if at any point 
                the number is over 
            '''
            should_add = False
            while y < len(matrix[0]) and matrix[x][y].isdigit():
                print(x, y)
                curr_num += matrix[x][y]
                if is_touching_symbol(matrix, x, y, symbols): should_add = True
                y += 1

            if curr_num != "":
                if should_add: summ += int(curr_num)
            else:
                y += 1
            curr_num = ""

    print(summ)


def solve_part_2(input_file):
    file = open(input_file, 'r').read()
    matrix = [list(line) for line in file.split('\n')]

    gears = {} #key is pos of gear as tuple and value is list
    for x in range(len(matrix)):
        # looking for a number in the line
        curr_num = ""
        y = 0
        while y < len(matrix[0]):
            '''
                lookgin for a digit. Need to reset if at any point 
                the number is over 
            '''
            pos_gear = ()
            while y < len(matrix[0]) and matrix[x][y].isdigit():
                curr_num += matrix[x][y]
                if pos_gear == () : pos_gear = pos_touching_gear(matrix, x, y)
                # WARNING: if multiple gears for a single number=>doesnot work
                y += 1

            if curr_num != "":
                if pos_gear != () and pos_gear not in gears:
                    # print(pos_gear)
                    gears[pos_gear] = [int(curr_num)]
                elif pos_gear != ():
                    gears[pos_gear].append(int(curr_num))
            else:
                y += 1
            curr_num = ""     
    # now check if a gear is touching more than 1 number
    # if yes multiple them and add it to total sum
    summ = 0
    for key, value in gears.items():
        mult = 1
        if len(value) > 1:
            for v in value: mult *= v
        if mult > 1: summ += mult
    print(summ)
    
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    logging.info(f"Elapsed in {1000*(end-start)} secondes")