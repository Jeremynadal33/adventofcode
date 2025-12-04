import time
from commons.utils import args, logging

from PIL import Image, ImageDraw, ImageFont

def main():
    file_path = (
        f"adventofcode{args.YEAR}/inputs/input_day{args.DAY}.txt"
        if args.INPUT == "REAL"
        else f"adventofcode{args.YEAR}/inputs/test_day{args.DAY}.txt"
    )
    solve_puzzle(input_file=file_path, part=args.PART)


def solve_puzzle(input_file, part):
    logging.info(f"Solving puzzle part {args.DAY}")
    if part == 1:
        solve_part_1(input_file)
    elif part == 2:
        solve_part_2(input_file)


def solve_part_1(input_file):
    file = open(input_file, "r").read().split("\n")

    max_around = 4
    count_free, new_grid = nb_free_spots(file, max_around)

    with open(f"adventofcode2025/outputs/day4_output_{args.INPUT}.txt", "w") as f:
        for line in new_grid:
            f.write(f"{line}\n")

    logging.info(f"Number of free spots: {count_free}")

def nb_free_spots(grid, max_around):
    count_free = 0
    new_grid = grid.copy()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            logging.debug(f"Checking position {(i, j)} with value {grid[i][j]}")
            if grid[i][j] == '.':
                continue
            elif grid[i][j] == 'x':
                new_grid[i] = new_grid[i][:j] + '.' + new_grid[i][j+1:]
            else:
                nb_around_value = nb_around(grid, i, j)
                if nb_around_value < max_around:
                    count_free += 1
                    new_grid[i] = new_grid[i][:j] + 'x' + new_grid[i][j+1:]
    logging.info(f"Found {count_free} new free spots in this iteration")
    return count_free, new_grid

def nb_around(grid, i, j):
    around = 0
    if i == 0 and j == 0: # Top left corner
        around += 1 if grid[i - 1][j + 1] == '@' else 0
        around += 1 if grid[  i  ][j + 1] == '@' else 0
        around += 1 if grid[i + 1][  j  ] == '@' else 0
    elif i == 0 and j == len(grid[i]) - 1: # Top right corner
        around += 1 if grid[  i  ][j - 1] == '@' else 0
        around += 1 if grid[i + 1][j - 1] == '@' else 0
        around += 1 if grid[i + 1][  j  ] == '@' else 0
    elif j == 0 and i == len(grid) - 1: # Bottom left corner
        around += 1 if grid[i - 1][  j  ] == '@' else 0
        around += 1 if grid[i - 1][j + 1] == '@' else 0
        around += 1 if grid[  i  ][j - 1] == '@' else 0
    elif i == len(grid) - 1 and j == len(grid[i]) - 1: # Bottom right corner
        around += 1 if grid[i - 1][  j  ] == '@' else 0
        around += 1 if grid[i - 1][j - 1] == '@' else 0
        around += 1 if grid[  i  ][j - 1] == '@' else 0
    elif i == 0: # Top edge
        around += 1 if grid[  i  ][j - 1] == '@' else 0
        around += 1 if grid[i + 1][j - 1] == '@' else 0
        around += 1 if grid[i + 1][  j  ] == '@' else 0
        around += 1 if grid[i + 1][j + 1] == '@' else 0
        around += 1 if grid[  i  ][j + 1] == '@' else 0
    elif j == 0: # Left edge
        around += 1 if grid[i - 1][  j  ] == '@' else 0
        around += 1 if grid[i - 1][j + 1] == '@' else 0
        around += 1 if grid[  i  ][j + 1] == '@' else 0
        around += 1 if grid[i + 1][j + 1] == '@' else 0
        around += 1 if grid[i + 1][  j  ] == '@' else 0
    elif j == len(grid[i]) - 1: # Right edge
        around += 1 if grid[i - 1][  j  ] == '@' else 0
        around += 1 if grid[i - 1][j - 1] == '@' else 0
        around += 1 if grid[  i  ][j - 1] == '@' else 0
        around += 1 if grid[i + 1][j - 1] == '@' else 0
        around += 1 if grid[i + 1][  j  ] == '@' else 0
    elif i == len(grid) - 1: # Bottom edge
        around += 1 if grid[  i  ][j - 1] == '@' else 0
        around += 1 if grid[i - 1][j - 1] == '@' else 0
        around += 1 if grid[i - 1][  j  ] == '@' else 0
        around += 1 if grid[i - 1][j + 1] == '@' else 0
        around += 1 if grid[  i  ][j + 1] == '@' else 0
    else: # Middle
        around += 1 if grid[i - 1][j - 1] == '@' else 0
        around += 1 if grid[i - 1][  j  ] == '@' else 0
        around += 1 if grid[i - 1][j + 1] == '@' else 0
        around += 1 if grid[  i  ][j - 1] == '@' else 0
        around += 1 if grid[  i  ][j + 1] == '@' else 0
        around += 1 if grid[i + 1][j - 1] == '@' else 0
        around += 1 if grid[i + 1][  j  ] == '@' else 0
        around += 1 if grid[i + 1][j + 1] == '@' else 0

    logging.debug(f"Number of '@' around position {(i, j)}: {around}")
    
    return around

def test_nb_around():
    file = """...
@.@
..@"""
    grid = file.split('\n')
    logging.debug(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            logging.debug(f"Position {(i, j)} has {nb_around(grid, i, j)} around")


def solve_part_2(input_file):
    file = open(input_file, "r").read().split("\n")

    max_around = 4
    count_freed = 0
    new_free = 1 # any > 0 number to enter
    iteration = 0
    grid = file.copy()
    while new_free > 0:
        new_free, new_grid = nb_free_spots(grid, max_around)
        with open(f"adventofcode2025/outputs/day4_output_{args.INPUT}_{iteration}.txt", "w") as f:
            for line in new_grid:
                f.write(f"{line}\n")
        count_freed += new_free
        grid = new_grid.copy()
        iteration += 1
        logging.info(f"After iteration {iteration}, freed {new_free} spots")
    

    logging.info(f"Number of free spots: {count_freed}")

def turn_txt_to_png():
    from pathlib import Path
    from pygments.formatters import ImageFormatter
    import os
    import pygments.lexers
    
    lexer = pygments.lexers.TextLexer()
    folder_path = f"adventofcode2025/outputs/"
    for filename in os.listdir(folder_path):
        if filename.startswith(f"day4_output_") and filename.endswith('.txt'):
            iteration_num = filename.split('_')[-1].replace('.txt', '')
            txt_content = Path(folder_path + filename).read_text()
            png = pygments.highlight(txt_content, lexer, ImageFormatter(line_numbers=False))
            Path(f'{folder_path}/output_{filename}.png').write_bytes(png)



if __name__ == "__main__":
    # start = time.time()
    # main()
    # end = time.time()
    # logging.info(f"Elapsed in {1000 * (end - start)} secondes")
    # test_nb_around()
    # test_image()
    turn_txt_to_png()