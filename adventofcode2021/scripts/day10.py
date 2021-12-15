
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
    file = open(input, 'r').read().split('\n')
    incorrect_chars = []
    chunks = []
    for line in file:
        for char in line : 
            if char in ['[', '(', '{', '<']:
                chunks.append(char)
            elif char == ']' and chunks[-1] == '[' :
                chunks = chunks[:-1]
            elif char == '}' and chunks[-1] == '{' :
                chunks = chunks[:-1]
            elif char == ')' and chunks[-1] == '(' :
                chunks = chunks[:-1]
            elif char == '>' and chunks[-1] == '<' :
                chunks = chunks[:-1]
            else :
                incorrect_chars.append(char)
                break

    points = {')' : 3, ']': 57, '}': 1197, '>': 25137}
    sum = 0
    for char in incorrect_chars:
        sum += points[char]
    print(sum)


def solve_part_2(input):
    print('Solving puzzle part 2')
    file = open(input, 'r').read().split('\n')
    
    closings = []
    points = {'(' : 1, '[': 2, '{': 3, '<': 4}
    for line in file:
        is_correct_line = True
        chunks = []
        for char in line : 
            if char in ['[', '(', '{', '<']:
                chunks.append(char)
            elif char == ']' and chunks[-1] == '[' :
                chunks = chunks[:-1]
            elif char == '}' and chunks[-1] == '{' :
                chunks = chunks[:-1]
            elif char == ')' and chunks[-1] == '(' :
                chunks = chunks[:-1]
            elif char == '>' and chunks[-1] == '<' :
                chunks = chunks[:-1]
            else :
                is_correct_line = False
                break
        if is_correct_line:
            closings.append( count_points(chunks[::-1], points) )
    print(np.median(closings))
    

def count_points(closings, points):
    sum = 0 
    for char in closings:
        sum = 5*sum + points[char]
    return sum

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print('Elapsed in {} milisecondes'.format(1000*(end-start)))