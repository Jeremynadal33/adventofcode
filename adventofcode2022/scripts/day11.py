
import sys
import numpy as np
import time 
from functions import *
import math
from tqdm import tqdm

ops = {
    "+": (lambda x,y: x+y)
    , "-": (lambda x,y: x-y)
    , "*": (lambda x,y: x*y)
    , "/": (lambda x,y: x/y)
    }

def main():
    input_file, part = handle_args(sys.argv)
    solve_puzzle(input_file = input_file, part = part)

def solve_puzzle(input_file, part):
    if part == 1 :
        worry_drop = True
    elif part == 2 :
        worry_drop = False
    else: 
        print('part unknown')

    file = open(input_file, 'r').read().split('\n\n')

    Monkeys = []
    for item in file:
        Monkeys.append(Monkey(item.split('\n')))

    for monkey in Monkeys : monkey.describe()
    print('---------GOGOGOGO-----------')
    nb_round = 10000
    for _ in tqdm(range(nb_round)):
        for monkey in Monkeys:
            for _ in range(len(monkey.items_worry)):
                monkey_index, worry = monkey.send_item(worry_drop)
                Monkeys[monkey_index].get_item(worry)

    for monkey in Monkeys : monkey.describe()

    inspected = [monkey.nb_inspected for monkey in Monkeys]
    inspected.sort(reverse=True)
    print(inspected[0]*inspected[1])

# 2713310158

def get_operation(line):
    operation = line.split('=')[1].lstrip().split(' ')
    print( operation)
    first = operation[0]
    second = operation[2]
    operator = ops[operation[1]]
    if first == 'old' and second == 'old': return lambda x : operator(x, x)
    elif first == 'old': return lambda x : operator(x, int(second))
    elif second == 'old': return lambda x : operator(int(first), x)
    else : return lambda : operator(int(first), int(second))

def get_test(line):
    '''for the moment, it always test if it is divisible by someting'''
    return lambda x: x % int(line.split(' ')[-1]) == 0

class Monkey:
    def __init__(self, instructions):
        print(instructions[0].split(' '))
        self.index = int(instructions[0].split(' ')[1][0])
        self.items_worry = [int(item) for item in instructions[1].strip().split(':')[1].split(',')]
        self.operation = get_operation(instructions[2])
        self.test = get_test(instructions[3])
        '''always got true first'''
        self.index_next_monkey_test_true = int(instructions[4].split(' ')[-1])
        self.index_next_monkey_test_false = int(instructions[5].split(' ')[-1])
        self.nb_inspected = 0

    def describe(self):
        num_test = 26
        num_operation = 3
        print(f"Monkey {self.index} inspected {self.nb_inspected} items.\nHe currently has items with worry : {self.items_worry}.\nIts operation turns {num_operation} into {self.operation(num_operation)}.\nIts test turns {num_test} into {self.test(num_test)}\n\n")

    def send_item(self, worry_drop):
        '''
        First, monkey inspect first item in list so worry level increased by operation
        Then, monkey gets bored so worry level is divided by 3
        Finaly, monkey throws item acording to test
        return both the index of the monkey to throw and its current worry level'''
        self.nb_inspected += 1
        if worry_drop : self.items_worry[0] = math.floor( self.operation(self.items_worry[0]) / 3 )
        else : self.items_worry[0] = self.operation(self.items_worry[0])
        worry_item = self.items_worry.pop(0)
        index = self.index_next_monkey_test_true if self.test(worry_item) else self.index_next_monkey_test_false
        
        return index, worry_item

    def get_item(self, worry_item):
        self.items_worry.append(worry_item)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print('Elapsed in {} milisecondes'.format(1000*(end-start)))