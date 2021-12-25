
import sys
import numpy as np
import time 
from functions import *

def main():
    input_file, part = handle_args(sys.argv)
    solve_puzzle(input_file = input_file, part = part)

def solve_puzzle(input_file, part):
    if part == 1 :
        solve_part_1(input_file)
    elif part == 2 :
        solve_part_2(input_file)

def solve_part_1(input_file):
    print('Solving puzzle part 1')
    file_hexa = open(input_file, 'r').read()
    hex_dict = {
        '0' : '0000',
        '1' : '0001',
        '2' : '0010',
        '3' : '0011',
        '4' : '0100',
        '5' : '0101',
        '6' : '0110',
        '7' : '0111',
        '8' : '1000',
        '9' : '1001',
        'A' : '1010',
        'B' : '1011',
        'C' : '1100',
        'D' : '1101',
        'E' : '1110',
        'F' : '1111'
    }
    file_bins = ''.join([hex_dict[char] for char in file_hexa])
    
    print('Answer is : ', handle_main(file_bins))
    

def solve_part_2(input_file):
    print('Solving puzzle part 2')
    file = open(input_file, 'r').read().split('\n')
    
def handle_main(bins):
    versions = 0 
    version = handle_binary(bins[:3])
    versions += version
    type = handle_binary(bins[3:6])
    _, number, versions = handle_rest(6, type, bins, versions)
    return number, versions


def handle_subpackets(index, subpackets, versions):
    version = handle_binary(subpackets[index : index + 3])

    versions += version
    type = handle_binary(subpackets[index + 3 : index + 6])
    return handle_rest(index + 6, type, subpackets, versions)

def handle_binary(bin_number):
    decimal = 0
    for num in range(len(bin_number)):
        #going from the end is easier
        decimal += int(bin_number[-(num+1)])*2**num
    return decimal

def handle_rest(index, type, file, versions):
    if type == 4:
        literal = ''
        ended = False
        while index + 5 < len(file) and not ended :
            literal += file[index+1:index+5]
            if file[index] == '0' :
                ended = True
            index += 5
        print('got literal : ', handle_binary(literal))
        return index, handle_binary(literal), versions
    else:
        
        if file[index] == '0' :
            print('heeeere')
            # total length of subpackets
            sub_length = handle_binary(file[index + 1 : index + 16])
            print(file[index + 1 : index + 16])
            # for the moment lets suppose the opperators all add 
            summ = 0
            index += 16
            borne = index + sub_length
            print(index, borne, sub_length)
            while index < borne :
                index, to_add, versions = handle_subpackets(index, file, versions)
                summ += to_add 
            return index, summ, versions
            
        elif file[index] == '1' :
            # number of subpackets
            sub_length = handle_binary(file[index + 1 : index + 12])
            index += 12
            summ = 0 
            for _ in range(sub_length):
                index, to_add, versions = handle_subpackets(index, file, versions)
                summ += to_add 
            return index, summ, versions


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print('Elapsed in {} milisecondes'.format(1000*(end-start)))