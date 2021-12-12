
import sys
import numpy as np
import time 
from functions import *

def main():
    input_txt, part = handle_args(sys.argv)
    solve_puzzle(input = input_txt, part = part)

def solve_puzzle(input, part):
    ## Common to both parts : the reading of the file 
    file = open(input, 'r').read().split('\n')
    all_signals = []
    all_outputs = []
    for line in file :
        all_signals.append( [ Digit(rep) for rep in line.split(' | ')[0].split(' ') ] )
        all_outputs.append( [ Digit(rep) for rep in line.split(' | ')[1].split(' ') ] )       
    
    if part == 1 :
        solve_part_1(all_signals, all_outputs)
    elif part == 2 :
        solve_part_2(all_signals, all_outputs)

def solve_part_1(all_signals, all_outputs):
    print('Solving puzzle part 1')
    
    # only count easy parts 1s, 4s, 7s, 8s 
    count = 0 
    for output in all_outputs :
        for num in output : 
            if num.number != -1 :
                count += 1
    print(count)
    

def solve_part_2(all_signals, all_outputs):
    print('Solving puzzle part 2')
    decoded = []
    for ind in range(len(all_outputs)):
        digits = all_signals[ind]
        find_9(digits)
        find_5_6(digits)
        find_0(digits)
        find_3(digits)
        find_2(digits)
        decoded.append(decode(digits, all_outputs[ind]))

    print(sum(decoded))
def get_representation(digits, number):
    for digit in digits:
        if digit.number == number :
            return digit.representation


def find_9(digits):
    reprensation_9 = ''.join(set(get_representation(digits, 7)+get_representation(digits,4)))
    for digit in digits :
        if digit.check_in_representation(reprensation_9, 9):
            break

def find_5_6(digits):
    # Only one having abd and is of length 5
    rep7 = get_representation(digits, 7)
    rep4 = get_representation(digits, 4)
    for char in get_representation(digits,1):
        rep7 = rep7.replace(char, '')
        rep4 = rep4.replace(char, '')
    abd = rep7 + rep4
    for digit in digits :
        if digit.check_in_representation(abd, 6):
            
            #break
            pass

def find_0(digits):
    # at that point, the only one having 6 characters
    for digit in digits :
        if digit.check_length():
            pass

def find_3(digits):
    # at that point, the only one having 6 characters
    for digit in digits :
        rep1 = get_representation(digits, 1)
        if digit.check_in_representation(rep1, 3):
            pass

def find_2(digits):
    for digit in digits :
            if digit.number == -1 :
                digit.number = 2
                break

def decode(digits, outputs):
    code = ''
    for outpout in outputs:
        for digit in digits:
            if sorted(digit.representation) == sorted(outpout.representation):
                code += str(digit.number)
                
    return int(code)

class Digit:
    def __init__(self, representation):
        self.representation = representation
        self.number = -1
        self.possible_numbers =  self.init_possible_numbers(self)
        self.usual_representation = []

    def init_possible_numbers(self, representation):
        if len(self.representation) == 2:
            self.number = 1
            return [1]
        elif len(self.representation) == 3:
            self.number = 7
            return [7]
        elif len(self.representation) == 4:
            self.number = 4
            return [4]
        elif len(self.representation) == 5:
            return [2, 3, 5]
        elif len(self.representation) == 6:
            return [6, 9]
        elif len(self.representation) == 7:
            self.number = 8
            return [8]

    def check_exacte_representation(self, rep, number):
        if sorted(self.representation) == sorted(rep):
            self.number = number 
            return True 

    def check_in_representation(self, representation, number):
        if self.number == -1 : #make sure we havnt found already
            # if we are sure that the only representation possible is in representation
            number_correct_chars = 0
            for char in representation : 
                if char in self.representation:
                    number_correct_chars += 1 

            if number_correct_chars == len(representation):
                if number == 5 or number == 6 :
                    if len(self.representation) == 6: #additional check to see length
                        self.number = 6
                        return True 
                    elif len(self.representation) == 5:
                        self.number = 5
                        return True
                    else: 
                        return False
                elif number == 9 and len(representation) == len(self.representation) - 1 :
                    self.number = number
                    return True
                elif number == 3 :
                    self.number = 3
                    return True
                else:
                    return False
            else:
                return False

    def check_length(self):
        # if check length its to find 0 
        if self.number == -1:
            if len(self.representation) == 6 : 
                self.number = 0
                return True 
            else : return False 
        else : return False 


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print('Elapsed in {} milisecondes'.format(1000*(end-start)))