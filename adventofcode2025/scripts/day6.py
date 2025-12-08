import time
from commons.utils import args, logging
from commons.Grid import Grid

import re

class GridDay6(Grid):
    
    
    def __init__(self, file_path, col_delimiter = ",") -> None:
        super().__init__(file_path, col_delimiter= col_delimiter)

    def preprocess(self):
        lines = open(self.file_path, 'r').read().split('\n')
        result = ""
        for line in lines:
            result += re.sub(r'\s+', ',', line.strip()) + '\n'
        return result

OPERATION = {
    '*': lambda x, y: x * y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
}

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
    grid = GridDay6(input_file)
    results = []
    for j in range(grid.grid.shape[1]):
        operation = str(grid[-1, j])
        logging.debug(f"Processing column {j} with operation {operation}")
        
        init_nb = 1 if operation == "*" else 0
        for i in range(grid.grid.shape[0] - 1):
            init_nb = OPERATION[operation](init_nb, int(grid[i, j]))
        
        logging.info(f"Result for column {j}: {init_nb}")
        results.append(init_nb)
    logging.info(f"Final results: {sum(results)}")

def solve_part_2(input_file):
    grid = Grid(input_file)
    grid.display()
    problems = []
    pb_index = 0
    for j in range(grid.grid.shape[1]):
        if all(grid[:, j]== ' '):
            problems.append(grid[:, pb_index:j])
            pb_index = j + 1
    # we miss the last problem
    problems.append(grid[:, pb_index:])

    results = []
    for p in problems:
        operation = str(''.join(p[-1, :])).strip()
        rest = p[:-1, :]
        logging.debug(f"operation: {operation}, rest shape: {rest.shape}")
        init_nb = 1 if operation == "*" else 0

        logging.debug(f"Processing problem with operation {operation}")

        for i in range(rest.shape[1]):
            current_nb = int(''.join(rest[:, i]).strip())
            logging.debug(f"Processing column {i} with values {current_nb}")
            init_nb = OPERATION[operation](init_nb, current_nb)
        
        results.append(init_nb)

    logging.debug(f"Results per problem: {results}")
    logging.info(f"Final results: {sum(results)}")


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    logging.info(f"Elapsed in {1000 * (end - start)} secondes")
