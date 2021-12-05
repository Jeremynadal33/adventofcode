
import sys
from functions import *
import numpy as np
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
    file = open(input, 'r').read().split('\n')
    matrix = get_matrix_from_file(file)

    gamma_rate   = ''
    epsilon_rate = ''
    
    for index in range(matrix.shape[1]) : 
        bincounts = np.bincount(matrix[:,index])
        gamma_rate += str(np.argmax(bincounts))
        epsilon_rate += str(np.argmin(bincounts))
    print(gamma_rate, epsilon_rate)
    gamma_rate = handle_binary(gamma_rate)
    epsilon_rate = handle_binary(epsilon_rate)
    print('Gamma rate is {}, epsilon rate is {}.\nTheir multiplication is {}'.format(gamma_rate, epsilon_rate, gamma_rate*epsilon_rate))

def solve_part_2(input):
    print('Solving puzzle part 2')
    file = open(input, 'r').read().split('\n')
    matrix = get_matrix_from_file(file)

    O2 = get_life_support_rating(matrix, 'O2')
    CO2 = get_life_support_rating(matrix, 'CO2')
    decimal_O2 = handle_binary(O2)
    decimal_CO2 = handle_binary(CO2)
    
    print('Life support rating report :\nO2: {} or in decimal {}\nCO2: {} or in decimal : {}\nMultiplication: {}'.format(O2, decimal_O2, CO2, decimal_CO2, decimal_CO2*decimal_O2))

def get_matrix_from_file(file):
    matrix = []
    for line in file: 
        matrix.append( [ int(char) for char in line ] )
    matrix = np.array(matrix)
    return matrix


def get_life_support_rating(matrix, gaz):
    copied_matrix = matrix.copy()
    if gaz == 'O2': criteria = 'max'
    elif gaz == 'CO2': criteria = 'min'
    index = 0
    while copied_matrix.shape[0] > 1:
        copied_matrix = remove_lines(copied_matrix, index, criteria)
        index += 1

    str_matrix = ''
    for ind in range(copied_matrix[0].shape[0]):
        str_matrix += str(copied_matrix[0][ind])
    return str_matrix

def remove_lines(matrix, index, order):
    #first, get the bit criteria
    bincounts = np.bincount(matrix[:,index])
    
    if order == 'max':
        if bincounts[0] != bincounts[1]:
            criteria = np.argmax(bincounts)
        else : 
            criteria = 1
    elif order == 'min':
        if bincounts[0] != bincounts[1]:
            criteria = np.argmin(bincounts)
        else: 
            criteria = 0
    else : print('Order unknown')
   

    #then remove lines with criteria
    for line in range(matrix.shape[0])[::-1]:
        if matrix[line, index] != criteria:
            matrix = np.delete(matrix, line, axis=0)
    return matrix

def handle_binary(bin_number):
    decimal = 0
    for num in range(len(bin_number)):
        #going from the end is easier
        decimal += int(bin_number[-(num+1)])*2**num
    return decimal
    

if __name__ == "__main__":
    main()
    # print(handle_binary('11111'))
    # a = np.array([1, 2, 6, 4, 2, 3, 2])
    # print(np.__version__)
    # print(pd.__version__)
    # values, counts = np.unique(a, return_counts=True)
    # print(np.bincount( np.array( [1,1,0,0] ) ))
