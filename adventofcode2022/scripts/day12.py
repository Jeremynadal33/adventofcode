
import sys
import numpy as np
import time 
from functions import *
import networkx as nx
import matplotlib.pyplot as plt

def char_to_num(char):
    if char == 'S':
        return 1
    elif char == 'E':
        return 26
    else:
        return ord(char) - 96

def str_coord(x , y):
    return f"{x};{y}"

def should_add_edge(height_map, xi, yi, xe, ye):
    print('------------')
    print(xi, yi, height_map[xi][yi], char_to_num(height_map[xi][yi]))
    print(xe, ye, height_map[xe][ye], char_to_num(height_map[xe][ye]))
    print(char_to_num(height_map[xi][yi]) + 1 >= char_to_num(height_map[xe][ye]))
    return char_to_num(height_map[xi][yi]) + 1 >= char_to_num(height_map[xe][ye])

def get_map(file):
    '''dans un premier temps on parse les lignes
    dans un deuxieme temps on transpose le resultat pour avoir les x en premier et y en deuxieme'''
    file = file.split('\n')
    len_y = len(file)
    len_x = len(file[0])
    map = [[j for j in i] for i in file]
    array = np.array(map)
    transposed_array = array.T
    return transposed_array.tolist(), len_x, len_y

def get_graph(height_map, len_x, len_y):
    '''on parcourt toute la carte et on ajoute les liens entre les noeuds si jamais on peut y passer
    pour unicité, on utilise les coordonnées'''
    G = nx.DiGraph()
    for x in range(len_x):
        for y in range(len_y):
            if height_map[x][y] == 'S': start_coord = str_coord(x, y)
            if height_map[x][y] == 'E': end_coord = str_coord(x, y)
            G.add_node(f"{x};{y}")
            if x == 0 and y == 0: #en haut à gauche
                if should_add_edge(height_map, x, y, x +1, y): G.add_edge(str_coord(x, y), str_coord(x+1, y))
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x][y+1]): G.add_edge(str_coord(x, y), str_coord(x, y+1))
            elif x == len_x - 1 and y == len_y - 1: #en bas à droite
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x-1][y]): G.add_edge(str_coord(x, y), str_coord(x-1, y))
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x][y-1]): G.add_edge(str_coord(x, y), str_coord(x, y-1))
            elif x == 0 and y == len_y - 1: #en bas à gauche
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x+1][y]): G.add_edge(str_coord(x, y), str_coord(x+1, y))
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x][y-1]): G.add_edge(str_coord(x, y), str_coord(x, y-1))
            elif y == 0 and x == len_x -1: #en haut à droite 
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x-1][y]): G.add_edge(str_coord(x, y), str_coord(x-1, y))
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x][y+1]): G.add_edge(str_coord(x, y), str_coord(x, y+1))
            elif x == 0 : # à gauche
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x+1][y]): G.add_edge(str_coord(x, y), str_coord(x+1, y))
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x][y+1]): G.add_edge(str_coord(x, y), str_coord(x, y+1))
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x][y-1]): G.add_edge(str_coord(x, y), str_coord(x, y-1))
            elif x == len_x - 1 : # à droite
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x-1][y]): G.add_edge(str_coord(x, y), str_coord(x-1, y))
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x][y+1]): G.add_edge(str_coord(x, y), str_coord(x, y+1))
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x][y-1]): G.add_edge(str_coord(x, y), str_coord(x, y-1))
            elif y == 0: #en haut
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x+1][y]): G.add_edge(str_coord(x, y), str_coord(x+1, y))
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x-1][y]): G.add_edge(str_coord(x, y), str_coord(x-1, y))
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x][y+1]): G.add_edge(str_coord(x, y), str_coord(x, y+1))
            elif y == len_y - 1: #en bas
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x+1][y]): G.add_edge(str_coord(x, y), str_coord(x+1, y))
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x-1][y]): G.add_edge(str_coord(x, y), str_coord(x-1, y))
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x][y-1]): G.add_edge(str_coord(x, y), str_coord(x, y-1))
            else :
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x+1][y]): G.add_edge(str_coord(x, y), str_coord(x+1, y))
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x-1][y]): G.add_edge(str_coord(x, y), str_coord(x-1, y))
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x][y+1]): G.add_edge(str_coord(x, y), str_coord(x, y+1))
                if char_to_num(height_map[x][y]) + 1 >= char_to_num(height_map[x][y-1]): G.add_edge(str_coord(x, y), str_coord(x, y-1))
    return G, start_coord, end_coord

def get_all_starting_pos(height_map, len_x, len_y, start_coord):
    res = [start_coord]
    for x in range(len_x):
        for y in range(len_y):
            if height_map[x][y] == 'a': res.append(str_coord(x, y))
    return res

def main():
    input_file, part = handle_args(sys.argv)
    solve_puzzle(input_file = input_file, part = part)

def solve_puzzle(input_file, part):
    if part == 1 :
        solve_part_1(input_file)
    elif part == 2 :
        solve_part_2(input_file)

def solve_part_1(input_file):
    print('Solving puzzle part 1')
    file = open(input_file, 'r').read()
    height_map, len_x, len_y = get_map(file)

    G, start_coord, end_coord = get_graph(height_map, len_x, len_y)
    print(start_coord, end_coord)
    # pos = nx.spring_layout(G, iterations=1000, seed=39775)

    # nx.draw(G, pos, with_labels=True)
    # plt.show()
    short = nx.shortest_path(G, start_coord, end_coord)
    print(len(nx.shortest_path(G, start_coord, end_coord))-1) #on enleve la première case car on veut le nbr de step
    print(short)

def solve_part_2(input_file):
    print('Solving puzzle part 2')
    file = open(input_file, 'r').read()
    height_map, len_x, len_y = get_map(file)

    G, start_coord, end_coord = get_graph(height_map, len_x, len_y)
    print(start_coord, end_coord)
    
    start_coords = get_all_starting_pos(height_map, len_x, len_y, start_coord)

    lengths = []
    for init in start_coords:
        try:
            lengths.append(len(nx.shortest_path(G, init, end_coord)) - 1 ) #on enleve la première case car on veut le nbr de step
        except:
            print(f"No path from {init} and {end_coord}")
    print(min(lengths))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print('Elapsed in {} milisecondes'.format(1000*(end-start)))