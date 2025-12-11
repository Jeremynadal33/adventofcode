import time
from commons.utils import args, logging

from commons.Grid import Grid
import numpy as np

def main():
    file_path = (
        f"adventofcode{args.YEAR}/inputs/input_day{args.DAY}.txt"
        if args.INPUT == "REAL"
        else f"adventofcode{args.YEAR}/inputs/test_day{args.DAY}_bis.txt"
    )
    solve_puzzle(input_file=file_path, part=args.PART)


def solve_puzzle(input_file, part):
    logging.info(f"Solving puzzle part {args.DAY}")
    if part == 1:
        solve_part_1(input_file)
    elif part == 2:
        solve_part_2(input_file)


def solve_part_1(input_file):
    grid = Grid(input_file, col_delimiter=",", item_type=int)

    logging.debug(f"Grid loaded from {grid}:")
    areas = []

    for i in range(grid.grid.shape[0]):
        for j in range(i + 1, grid.grid.shape[0]):
            x1, y1 = grid.grid[i]
            x2, y2 = grid.grid[j]
            area = (1 + abs(x1 - x2)) * (1 + abs(y1 - y2))
            logging.debug(f"Comparing point {i} and point {j}: {grid.grid[i]} vs {grid.grid[j]} with area of {area}")
            areas.append(area)
    
    logging.info(f"Largest area found: {max(areas)}")
    

def solve_part_2(input_file):
    inputs = Grid(input_file, col_delimiter=",", item_type=int)

    # i think input and the way i construct grids is transposed they have (col, row)
    max_grid_cols = inputs.grid[:,0].max() + 1
    max_grid_rows = inputs.grid[:,1].max() + 1

    logging.debug(f"max_grid_rows: {max_grid_rows}, max_grid_cols: {max_grid_cols}")

    rows = { i: {"min_y":float('inf'), "max_y": -float('inf')} for i in range(max_grid_rows) }
    cols = { i: {"min_x":float('inf'), "max_x": -float('inf')} for i in range(max_grid_cols) }

    # on peut avancer de 1 en 1 depuis le point de départ jusqu'au prochain point pour tracer des lignes
    # et avoir les min et max par ligne et colonne

    y, x = inputs.grid[0]
    logging.debug(f"Initial point: ({x}, {y})")
    rows[x]["min_y"] = min(rows[x]["min_y"], y)
    rows[x]["max_y"] = max(rows[x]["max_y"], y)
    cols[y]["min_x"] = min(cols[y]["min_x"], x)
    cols[y]["max_x"] = max(cols[y]["max_x"], x)


    # handle last point to first point to close the loop at first iteration
    for point_idx in range(inputs.grid.shape[0]): # col, row
        yp, xp = inputs.grid[point_idx - 1] # previous point
        y, x = inputs.grid[point_idx]

        logging.debug(f"going from point ({xp}, {yp}) to point ({x}, {y})")
        # each step either x or y changes
        if xp == x: #horizontal move
            step = 1 if y > yp else -1
            for yy in range(yp, y + step, step):
                logging.debug(f"  updating row {x} at y={yy}")
                rows[x]["min_y"] = min(rows[x]["min_y"], yy)
                rows[x]["max_y"] = max(rows[x]["max_y"], yy)
                cols[yy]["min_x"] = min(cols[yy]["min_x"], x)
                cols[yy]["max_x"] = max(cols[yy]["max_x"], x)
        elif yp == y: #vertical move
            step = 1 if x > xp else -1
            for xx in range(xp, x + step, step):
                logging.debug(f"  updating column {y} at x={xx}")
                rows[xx]["min_y"] = min(rows[xx]["min_y"], y)
                rows[xx]["max_y"] = max(rows[xx]["max_y"], y)
                cols[y]["min_x"] = min(cols[y]["min_x"], xx)
                cols[y]["max_x"] = max(cols[y]["max_x"], xx)
        else:
            logging.error(f"Unexpected move from ({xp}, {yp}) to ({x}, {y}) that is neither horizontal nor vertical")

    if args.INPUT == "TEST": 
        print_grid(rows, cols)
        logging.info(rows)
        logging.info(cols)

    areas = []

    for i in range(inputs.grid.shape[0]):
        for j in range(i + 1, inputs.grid.shape[0]):
            # getting y, x position because matrix is transposed compared to my representation
            # y1 = int(inputs.grid[i][0])
            # x1 = int(inputs.grid[i][1])
            # y2 = int(inputs.grid[j][0])
            # x2 = int(inputs.grid[j][1])
            # x1, y1 = inputs.grid[i]
            # x2, y2 = inputs.grid[j]
            y1, x1 = inputs.grid[i]
            y2, x2 = inputs.grid[j]
            logging.debug(f"Comparing point {i} and point {j}: {inputs.grid[i][::-1]} vs {inputs.grid[j][::-1]}")

            
            if is_in_area(int(x1), int(y1), int(x2), int(y2), rows, cols):
                area = (1 + abs(x1 - x2)) * (1 + abs(y1 - y2))
                logging.debug(f"Rectangle is in area between point {i} and point {j} is {area}")
                areas.append(area)            
    
    logging.info(f"Largest area found: {max(areas)} \nShould be less than 4633542570 for real input\n")

def is_point_in_area(x, y, rows, cols):
    return rows[x]["min_y"] <= y <= rows[x]["max_y"] and cols[y]["min_x"] <= x <= cols[y]["max_x"]

def is_in_area(x1, y1, x2, y2, rows, cols):
    ##
    # condition_on_rows = ( ( (y1 <= y2) and (rows[x1]["max_y"] >= y2) ) or ( (y1 > y2) and (rows[x1]["min_y"] >= y2) ) )
    # condition_on_cols = ( ( (x1 <= x2) and (cols[y1]["max_x"] >= x2) ) or ( (x1 > x2) and (cols[y1]["min_x"] >= x2) ) )
    # logging.debug(f"  Checking is_in_area for points ({x1}, {y1}) to ({x2}, {y2}): condition_on_cols={condition_on_cols}, condition_on_rows={condition_on_rows}")
    # return condition_on_cols and condition_on_rows

    ## Maybe we should just check that the two opposite corners are in the area defined by rows and cols

    ## NOT ENOUGH because we could have a U shape that would include both corners but not the full rectangle
    is_in = True
    # Check all exterior points
    # top edge
    for y in range(min(y1, y2), max(y1, y2) + 1):
        if not is_point_in_area(x1, y, rows, cols):
            logging.debug(f"  Point ({x1}, {y}) on left edge is out of area")
            return False
    # bottom edge
    for y in range(min(y1, y2), max(y1, y2) + 1):
        if not is_point_in_area(x2, y, rows, cols):
            logging.debug(f"  Point ({x2}, {y}) on right edge is out of area")
            return False
    # left edge
    for x in range(min(x1, x2), max(x1, x2) + 1):
        if not is_point_in_area(x, y1, rows, cols):
            logging.debug(f"  Point ({x}, {y1}) on top edge is out of area")
            return False
    # right edge
    for x in range(min(x1, x2), max(x1, x2) + 1):
        if not is_point_in_area(x, y2, rows, cols):
            logging.debug(f"  Point ({x}, {y2}) on bottom edge is out of area")
            return False
    return is_in


def print_grid(rows, cols):
    grid = np.array([['.' for _ in range(len(cols) + 2)] for _ in range(len(rows) + 1)])
    for r in range(len(rows)):
        for c in range(len(cols)):
            if is_point_in_area(r, c, rows, cols):
                grid[r][c] = '#'
    
    logging.info("Current grid state:")
    for row in grid:
        logging.info("".join(row))


######################### TESTS #########################

def test_is_in_area():
    rows = {0: {'min_y': float('inf'), 'max_y': -float('inf')}, 1: {'min_y': 7, 'max_y': 11}, 2: {'min_y': 7, 'max_y': 11}, 3: {'min_y': 2, 'max_y': 11}, 4: {'min_y': 2, 'max_y': 11}, 5: {'min_y': 2, 'max_y': 11}, 6: {'min_y': 9, 'max_y': 11}, 7: {'min_y': 9, 'max_y': 11}}
    cols = {0: {'min_x': float('inf'), 'max_x': -float('inf')}, 1: {'min_x': float('inf'), 'max_x': -float('inf')}, 2: {'min_x': 3, 'max_x': 5}, 3: {'min_x': 3, 'max_x': 5}, 4: {'min_x': 3, 'max_x': 5}, 5: {'min_x': 3, 'max_x': 5}, 6: {'min_x': 3, 'max_x': 5}, 7: {'min_x': 1, 'max_x': 5}, 8: {'min_x': 1, 'max_x': 5}, 9: {'min_x': 1, 'max_x': 7}, 10: {'min_x': 1, 'max_x': 7}, 11: {'min_x': 1, 'max_x': 7}}
    
    # logging.debug(rows)
    # logging.debug(cols)
    
    assert is_in_area(3, 2, 5, 9, rows, cols) == True
    assert is_in_area(1, 7, 7, 11, rows, cols) == False
    assert is_in_area(5, 2, 1, 11, rows, cols) == False
    assert is_in_area(5, 9, 3, 2, rows, cols) == True
    assert is_in_area(7, 9, 5, 9, rows, cols) == True
    assert is_in_area(3, 7, 1, 11, rows, cols) == True

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    logging.info(f"Elapsed in {end - start} secondes")
    test_is_in_area()

