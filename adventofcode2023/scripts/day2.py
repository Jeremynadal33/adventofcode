import time
from commons.utils import args, logging
import re

def main():
    file_path = f"adventofcode{args.YEAR}/inputs/input_day{args.DAY}.txt" if args.INPUT == "REAL" else f"adventofcode{args.YEAR}/inputs/test_day{args.DAY}.txt" 
    solve_puzzle(input_file = file_path, part = args.PART)

def solve_puzzle(input_file, part):
    logging.info(f"Solving puzzle part {args.PART}")
    if part == 1 :
        solve_part_1(input_file)
    elif part == 2 :
        solve_part_2(input_file)


def handle_show(shown):
    dict_shown = {"green": 0, "blue": 0, "red": 0}
    for color in shown.split(','):
        num = int(re.sub("[a-z]", "", color))
        for key in dict_shown.keys():
            if key in color:
                dict_shown[key] = num
    return dict_shown

def handle_line(line):
    splited = line.split(':')
    game_id = int(re.sub("[a-zA-Z]", "", splited[0]))
    max_shown = {"green": 0, "blue": 0, "red": 0}
    for show in splited[1].split(';'):
        dict_shown = handle_show(shown=show)
        for key, value in max_shown.items():
            if value < dict_shown[key]: max_shown[key] = dict_shown[key]
    return game_id, max_shown

def solve_part_1(input_file):
    file = open(input_file, 'r').read().split('\n')
    cube_config = {"green": 13, "blue": 14, "red": 12}
    summ = 0

    for line in file:
        game_id, max_shown = handle_line(line)
        possible = True
        for key, value in cube_config.items():
            if value < max_shown[key]: possible = False
        if possible: summ += game_id
        
    
    logging.info(f"Sum of all game ids {summ}")

def solve_part_2(input_file):
    file = open(input_file, 'r').read().split('\n')
    summ = 0

    for line in file:
        game_id, max_shown = handle_line(line)
        mult = 1
        for value in max_shown.values():
            mult *= value
        summ += mult
        
    logging.info(f"Sum of all game ids {summ}")       
    
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    logging.info(f"Elapsed in {1000*(end-start)} secondes")