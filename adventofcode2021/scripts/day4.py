
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

def solve_part_1(input):
    print('Solving puzzle part 1')
    file = open(input, 'r').read().split('\n\n')
    numbers = file[0].split(',')
    boards = []

    for ind in range(1, len(file)):
        boards.append(Bingo_board(handle_input_board(file[ind])))

    for num in numbers:
        for board in boards:
            print('\n\n\n')
            print(board.board)
            print(num)
            board.add_pin(float(num))
            if board.check_board():
                print('Number is {}, sum of unmarked numbers is {}.\nMultiplication is {} '.format(board.calculate_board(), num, num*board.calculate_board()))        
                break

def solve_part_2(input):
    print('Solving puzzle part 2')
    file = open(input, 'r').read().split('\n')


def handle_input_board(str_board):
        temp_file = open('temp.txt', 'w')
        temp_file.write(str_board)
        temp_file.close()
        board = np.loadtxt('temp.txt')
        return board

class Bingo_board:
    def __init__(self, board):
        self.board = board
        self.pinged_board = np.zeros((5,5), dtype=np.int8) #default is one and turn to 0 if ping
        self.has_won = False 
        self.axis = -1 #if won, either 0 or 1 to get the axis
        self.index = -1 #if won, index of the column/row of win

    def add_pin(self, number):
        x, y = np.where(self.board==number) 
        if not x.shape[0] == 0:
            self.pinged_board[x,y] = 1

    def check_board(self):
        # check rows first
        for axis in [0, 1]:
            index = np.where( np.sum(self.pinged_board, axis = axis) == self.pinged_board.shape[0] )[0]
            if not index.shape[0] == 0:
                self.has_won = True
                self.axis = axis
                self.index = index[0]
                self.calculate_board()
        return self.has_won
        
    def calculate_board(self):
        print(np.sum(self.board, where=self.pinged_board==0))
        return np.sum(self.board, where=self.pinged_board==0)

    

if __name__ == "__main__":
    main()
    