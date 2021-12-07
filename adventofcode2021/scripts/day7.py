
import sys
import numpy as np
import time 
from functions import *
import matplotlib.pyplot as plt
import pandas as pd

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
    file = open(input, 'r').read().split(',')
    crabs = [int(item) for item in file]
    df = pd.DataFrame(crabs)
    q1, q2, q3 = df.quantile([0.25, 0.5, 0.75])[0]
    q1, q3 = int(q1), int(q3)
    print( 'Looking for the minimum in the IQR : ', q1, q3)
    fuel = []
    fuel_2 = []
    for index in range(q1, q3 + 1):
        fuel.append(count_fuel(crabs, index))
        fuel_2.append(count_fuel_2(crabs, index))
    min_fuel = min(fuel)
    min_fuel_2 = min(fuel_2)
    print('For part 1, the minimum fuel between {} and {} is {} obtain for position {}'.format(q1, q3, min_fuel, q1 + fuel.index(min_fuel)))
    print('For part 2, the minimum fuel between {} and {} is {} obtain for position {}'.format(q1, q3, min_fuel_2, q1 + fuel_2.index(min_fuel_2)))

    print('Median was ', q2)
    end = time.time()
    print('Elapsed in {} milisecondes'.format(1000*(end-start)))

def count_fuel(list, index):
    return sum( [abs(item - index) for item in list] )

def count_fuel_2(list, index):
    # sum = 0
    # for item in list : 
    #     print('For ', item, ' to ', index)
    #     diff = abs(item - index)
    #     sum += diff*(diff+1)/2
    #     print( diff )
    #     print( diff*(diff + 1 )/2 )
    #     print('____________________')
    # return sum
    return sum(  [ (abs(item - index))*(abs(item - index)+1)/2 for item in list ]  )  

def solve_part_2(input):
    print('Solved in part 1')
    
if __name__ == "__main__":
    main()