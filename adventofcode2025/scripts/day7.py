import time
import random
from commons.utils import args, logging
from commons.Grid import Grid

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
    grid = Grid(input_file)
    nb_split = 0
    for i in range(1, grid.grid.shape[0]):
        for j in range(grid.grid.shape[1]):
            if grid[i - 1, j] == "S":
                grid[i, j] = "|"
            elif grid[i - 1, j] == "|" and grid[i, j] != "^":
                grid[i, j] = "|"
            elif grid[i - 1, j] == "|" and grid[i, j] == "^":
                nb_split += 1
                grid[i, j - 1] = "|"
                grid[i, j + 1] = "|"

    logging.debug(f"Final grid:\n{grid.__repr__()}")
    logging.info(f"Splitted {nb_split} times")

def solve_part_2(input_file):
    grid = Grid(input_file)

    paths = set()

    for _ in range(10000):
        to_cross = grid.copy()
        path = random_grid_crossing(to_cross)
        paths.add(tuple(path))

    logging.debug(f"Paths found: {paths}")
    logging.info(f"Number of unique paths: {len(paths)}")

    # for i in range(1, grid.grid.shape[0]):
    #     for j in range(grid.grid.shape[1]):
    #         possibilities_length = len(possibilities)
    #         logging.debug(f"Processing position {(i, j)} with {possibilities_length} possibilities")
    #         for p in range(possibilities_length):
    #             if possibilities[p][i - 1, j] == "S":
    #                 possibilities[p][i, j] = "|"
    #             elif possibilities[p][i - 1, j] == "|" and possibilities[p][i, j] != "^":
    #                 possibilities[p][i, j] = "|"
    #             elif possibilities[p][i - 1, j] == "|" and possibilities[p][i, j] == "^":
    #                 nb_split += 1
    #                 left_grid = possibilities[p]
    #                 right_grid = possibilities[p]
    #                 left_grid[i, j - 1] = "|"
    #                 right_grid[i, j + 1] = "|"
    #                 if left_grid not in possibilities: possibilities.append(left_grid)
    #                 if right_grid not in possibilities: possibilities.append(right_grid)

def random_grid_crossing(grid: Grid):
    path = []
    for i in range(1, grid.grid.shape[0]):
        for j in range(grid.grid.shape[1]):
            if grid[i - 1, j] == "S":
                grid[i, j] = "|"
                path.append((i, j))
            elif grid[i - 1, j] == "|" and grid[i, j] != "^":
                grid[i, j] = "|"
                path.append((i, j))
            elif grid[i - 1, j] == "|" and grid[i, j] == "^":
                # randomly choose left or right
                if random.choice([True, False]):
                    grid[i, j - 1] = "|"
                    path.append((i, j - 1))
                else:
                    grid[i, j + 1] = "|"
                    path.append((i, j + 1))
    return path

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    logging.info(f"Elapsed in {1000 * (end - start)} secondes")
