import time
from commons.utils import args, logging
from commons.Grid import Grid
from math import sqrt
import networkx as nx

import matplotlib.pyplot as plt

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
    coords = Grid(input_file, col_delimiter=",", item_type=int)
    logging.info(f"Coordinates loaded: {coords}")
    distances = make_distance_dictionary(coords)
    sorted_distances = dict(sorted(distances.items(), key=lambda item: item[1]))

    G = nx.Graph()
    for i in range(coords.grid.shape[0]): G.add_node(i)

    max_iterations = 10 if args.INPUT == "TEST" else 1000
    for index, key in enumerate(sorted_distances):
        if index >= max_iterations:
            break

        logging.debug(f"Next shortest distance: {key} with value {sorted_distances[key]}")
        # Connect points coords into existing clusters
        point1_idx, point2_idx = key
        G.add_edge(point1_idx, point2_idx)

        logging.debug(f"Is connected: {nx.is_connected(G)}")

    logging.debug(f"Graph nodes: {G.nodes}")
    logging.debug(f"Graph edges: {G.edges}")

    logging.info(f"Number of clusters: {nx.number_connected_components(G)}")


    result = 1

    cluster_sizes = []
    for sub in nx.connected_components(G):
        logging.info(f"Cluster: {sub}")
        cluster_sizes.append(len(sub))

    # Multiply sizes of the three largest clusters
    cluster_sizes.sort(reverse=True)
    for size in cluster_sizes[:3]:
        result *= size
    
    logging.info(f"Result: {result}")
    
    # subax1 = plt.subplot(121)
    # nx.draw(G, with_labels=True, font_weight='bold')
    # plt.show()



def make_distance_dictionary(coords):
    distance_dict = {}
    for i in range(coords.grid.shape[0]):
        for j in range(i + 1, coords.grid.shape[0]):
            coord1 = coords.grid[i]
            coord2 = coords.grid[j]
            distance = get_distance(coord1, coord2)
            distance_dict[(i, j)] = distance
    return distance_dict

def get_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2 + (coord1[2] - coord2[2]) ** 2)


def solve_part_2(input_file):
    coords = Grid(input_file, col_delimiter=",", item_type=int)
    logging.info(f"Coordinates loaded: {coords}")
    distances = make_distance_dictionary(coords)
    sorted_distances = dict(sorted(distances.items(), key=lambda item: item[1]))

    G = nx.Graph()
    for i in range(coords.grid.shape[0]): G.add_node(i)

    iterations = 0
    for index, key in enumerate(sorted_distances):
        logging.debug(f"Next shortest distance: {key} with value {sorted_distances[key]}")
        # Connect points coords into existing clusters
        point1_idx, point2_idx = key
        G.add_edge(point1_idx, point2_idx)
        logging.debug(f"Is connected: {nx.is_connected(G)}")
        iterations += 1
        if nx.is_connected(G):
            logging.info(f"Graph became connected after {iterations} iterations connecting {point1_idx} : {coords.grid[point1_idx]} and {point2_idx} : {coords.grid[point2_idx]}")
            logging.info(f"Final answer is then {coords.grid[point1_idx][0] * coords.grid[point2_idx][0]}")
            break



    logging.info(f"Number of clusters: {nx.number_connected_components(G)}")

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    logging.info(f"Elapsed in {end - start} secondes")
