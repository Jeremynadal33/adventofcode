import sys
import time
from functions import *

Rock = "Rock"
Paper = "Paper"
Scissors = "Scissors"
Draw = "Draw"
Win = "Win"
Loose = "Loose"
decrypt_opponent = {"A": Rock, "B": Paper, "C": Scissors}
decrypt_you = {"X": Rock, "Y": Paper, "Z": Scissors}

decrypt_strategy = {"X": Loose, "Y": Draw, "Z": Win}


def get_shape_points(you):
    if you == Rock:
        return 1
    elif you == Paper:
        return 2
    elif you == Scissors:
        return 3


def get_result_round(opponent, you):
    if opponent == you:
        return Draw
    elif opponent == Rock and you == Paper:
        return Win
    elif opponent == Rock and you == Scissors:
        return Loose
    elif opponent == Paper and you == Scissors:
        return Win
    elif opponent == Paper and you == Rock:
        return Loose
    elif opponent == Scissors and you == Rock:
        return Win
    elif opponent == Scissors and you == Paper:
        return Loose
    else:
        return "Unknown conf"


def get_result_points(opponent=Rock, you=Rock, part=1, result=None):
    if part == 1:
        result = get_result_round(opponent, you)

    if result == Win:
        return 6
    elif result == Draw:
        return 3
    elif result == Loose:
        return 0


def get_shape_strategy(opponent, strategy):
    if strategy == Draw:
        return opponent
    elif strategy == Win:
        if opponent == Rock:
            return Paper
        elif opponent == Paper:
            return Scissors
        elif opponent == Scissors:
            return Rock
    elif strategy == Loose:
        if opponent == Rock:
            return Scissors
        elif opponent == Paper:
            return Rock
        elif opponent == Scissors:
            return Paper
    else:
        return "Unknown startegy"


def get_round_points(opponent, you=Rock, part=1, strategy=None):
    if part == 1:
        return get_result_points(opponent, you) + get_shape_points(you)
    else:
        return get_result_points(part=part, result=strategy) + get_shape_points(
            get_shape_strategy(opponent=opponent, strategy=strategy)
        )


def main():
    input_file, part = handle_args(sys.argv)
    solve_puzzle(input_file=input_file, part=part)


def solve_puzzle(input_file, part):
    if part == 1:
        solve_part_1(input_file)
    elif part == 2:
        solve_part_2(input_file)


def solve_part_1(input_file):
    print("Solving puzzle part 1")
    file = open(input_file, "r").read().split("\n")

    sum = 0
    for item in file:
        print(item)
        opponent = decrypt_opponent[item[0]]
        you = decrypt_you[item[2]]
        sum += get_round_points(opponent, you)
    print(sum)


def solve_part_2(input_file):
    print("Solving puzzle part 2")
    file = open(input_file, "r").read().split("\n")

    sum = 0
    for item in file:
        print(item)
        opponent = decrypt_opponent[item[0]]
        strategy = decrypt_strategy[item[2]]
        print(opponent, strategy)
        sum += get_round_points(opponent=opponent, strategy=strategy, part=2)
    print(sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed in {} milisecondes".format(1000 * (end - start)))
