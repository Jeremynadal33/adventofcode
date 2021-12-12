
import sys
import numpy as np
import time 
from functions import *

def main():
    input_txt, part = handle_args(sys.argv)
    solve_puzzle(input = input_txt, part = part)

def solve_puzzle(input, part):
    matrix = np.genfromtxt(input, delimiter=1, dtype=int)
    print(matrix)
    lowests = []
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            # check if we are at the left border : 
            if x == 0 : 
                # check if we are at the top 
                if y == 0:
                    if matrix[x, y] < matrix[x+1,y] and matrix[x, y] < matrix[x,y+1]:
                        lowests.append((x,y))
                # check if we are at the bottom 
                elif y == matrix.shape[1] - 1 :
                    if matrix[x, y] < matrix[x+1,y] and matrix[x, y] < matrix[x,y-1]:
                        lowests.append((x,y))
                else : 
                    # on the left but not corner
                    if matrix[x, y] < matrix[x+1,y] and matrix[x, y] < matrix[x,y+1] and matrix[x,y] < matrix[x,y-1]:
                        lowests.append((x,y))
            # check if we are on the right border
            elif x == matrix.shape[0] - 1 :
                # check if we are at the top 
                if y == 0:
                    if matrix[x, y] < matrix[x-1,y] and matrix[x, y] < matrix[x,y+1]:
                        lowests.append((x,y))
                # check if we are at the bottom 
                elif y == matrix.shape[1] - 1 :
                    if matrix[x, y] < matrix[x-1,y] and matrix[x, y] < matrix[x,y-1]:
                        lowests.append((x,y))
                else : 
                    # on the right but not corner
                    if matrix[x, y] < matrix[x-1,y] and matrix[x, y] < matrix[x,y+1] and matrix[x,y] < matrix[x,y-1]:
                        lowests.append((x,y))
            # else we are not in a border
            else:
                # check if we are at the top 
                if y == 0:
                    if matrix[x, y] < matrix[x-1,y] and matrix[x, y] < matrix[x+1,y] and matrix[x, y] < matrix[x,y+1]:
                        lowests.append((x,y))
                # check if we are at the bottom 
                elif y == matrix.shape[1] - 1 :
                    if matrix[x, y] < matrix[x-1,y] and matrix[x, y] < matrix[x+1,y] and matrix[x, y] < matrix[x,y-1]:
                        lowests.append((x,y))
                else : 
                    # in the middle so search everywhere
                    if matrix[x, y] < matrix[x-1,y] and matrix[x, y] < matrix[x+1,y] and matrix[x, y] < matrix[x,y+1] and matrix[x,y] < matrix[x,y-1]:
                        lowests.append((x,y))
    if part == 1 :
        solve_part_1(matrix, lowests)
    elif part == 2 :
        solve_part_2(matrix, lowests)

def solve_part_1(matrix, lowests):
    print('Solving puzzle part 1')
    sum_lowests = 0
    for (x,y) in lowests:
        sum_lowests += matrix[x,y] + 1

    print(sum_lowests)
    print('Tere is {} bassins'.format(len(lowests)))

def solve_part_2(matrix, lowests):
    print('Solving puzzle part 2')
    # the bassin will record every position of the bassin, its size is gonna be len(bassin)
    # initially, it contains only the lowest height :
    
    bassins_size = []
    for lowest in lowests:
        print('\n\n____________________')
        print('____________________')
        bassin = [lowest] 
        bassin, new_locations = find_next_locations(matrix, bassin, *lowest)
        print(bassin, '--------', new_locations)
        next_locations = new_locations
        while len(next_locations) > 0:
            print('____________ new iteration ___________')
            all_new_locations = []
            for location in next_locations:
                print('For : \n')
                print(location)
                print('\n')
                bassin, new_locations = find_next_locations(matrix, bassin, *location)
                for location in new_locations:
                    if location not in all_new_locations:
                        all_new_locations.append(location)
            next_locations = all_new_locations
            
        bassins_size.append(len(set(bassin)))
    print(sorted(bassins_size))

def find_next_locations(matrix, bassin, x, y):
    # will look horizontally and vertically if there are other possibilities 
    # then for each possible locations, we begin again until there are 
    # nothing left 
    # WARNING : should check if we already went to 'new' or not ! 
    new_possible_locations = []
    # remember that position 0, 0 is top left of the matrix
    # First lets look upward : 
    up = x
    while up > 0 and matrix[up-1, y] > matrix[up, y] and matrix[up-1, y] != 9:
        print('up')
        new_possible_locations.append((up - 1, y))
        up -= 1
    # Then lets look downward : 
    down = x
    while down < matrix.shape[0] - 1 and matrix[down+1, y] > matrix[down, y] and matrix[down+1, y] != 9:
        print('down')
        new_possible_locations.append((down + 1, y))
        down += 1
    # First lets look left : 
    left = y
    while left > 0 and matrix[x, left-1] > matrix[x, left] and matrix[x, left-1] != 9:
        print('left')
        new_possible_locations.append((x, left-1))
        left -= 1
    # Then lets look right : 
    right = y
    while right < matrix.shape[1] - 1 and matrix[x, right+1] > matrix[x, right] and matrix[x, right+1] != 9:
        print('right')
        new_possible_locations.append((x, right+1))
        right += 1
    for location in new_possible_locations:
        if location in bassin:
            new_possible_locations.remove(location)
    bassin.extend(new_possible_locations)
    return bassin, new_possible_locations

        
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print('Elapsed in {} milisecondes'.format(1000*(end-start)))