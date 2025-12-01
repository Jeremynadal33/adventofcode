import sys
import numpy as np
import time
from functions import *
import networkx as nx


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
    matrix = np.genfromtxt(input_file, delimiter=1, dtype=int)

    G = nx.DiGraph()
    labeldict = {}
    labeltest = []
    test = np.zeros((matrix.shape[0], matrix.shape[1]))
    # first lets create the points
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            labeldict[str(x) + "," + str(y)] = matrix[x, y]
            labeltest.append(str(x) + "," + str(y))
            G.add_node(str(x) + "," + str(y), pos=(x, y))
            test[x, y] += 1

    # add horizontal edges :
    for x in range(matrix.shape[0] - 1):
        for y in range(matrix.shape[1]):
            G.add_edge(
                str(x) + "," + str(y),
                str(x + 1) + "," + str(y),
                weight=matrix[x + 1, y],
            )

    # add vertical edges :
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1] - 1):
            G.add_edge(
                str(x) + "," + str(y),
                str(x) + "," + str(y + 1),
                weight=matrix[x, y + 1],
            )

    # for x in range(matrix.shape[0]-1):
    #     for y in range(matrix.shape[1]-1):
    #         G.add_edge( str(x)+','+str(y), str(x+1)+','+str(y), weight = matrix[x+1, y] )
    #         G.add_edge( str(x)+','+str(y), str(x)+','+str(y+1), weight = matrix[x, y+1] )

    # # add edges grom last row/column
    # y = matrix.shape[1] - 1
    # for x in range(matrix.shape[0] - 1):
    #     G.add_edge( str(x)+','+str(y), str(x+1)+','+str(y), weight = matrix[x+1, y] )

    # x = matrix.shape[0] - 1
    # for y in range(matrix.shape[1] - 1):
    #     G.add_edge( str(x)+','+str(y), str(x)+','+str(y+1), weight = matrix[x, y+1] )

    ###############################################################@
    # print( len(np.where( test == 0 )[0]) )
    # print( len(labeldict) , matrix.shape[0]*matrix.shape[1], G.number_of_nodes() )
    # print(len(labeltest))

    # labels = [ item for item in labeltest ]
    # print(labeltest[0])
    # uniques, counts = np.unique(labels, return_counts=True)
    # doublons = np.where(counts>1)
    # for item in doublons:
    # print(uniques)
    # for x in range(matrix.shape[0]-1):
    #     for y in range(matrix.shape[1]-1):
    #         if x == 0 and y == 0:
    #             G.add_node( str(x)+','+str(y), pos = (x, y) )
    #             labeldict[str(x)+','+str(y)] = matrix[x, y]
    #         labeldict[str(x+1)+','+str(y)] = matrix[x+1, y]
    #         labeltest.append( str(x+1)+','+str(y) )
    #         test[x+1, y] += 1
    #         labeldict[str(x)+','+str(y+1)] = matrix[x, y+1]
    #         labeltest.append( str(x)+','+str(y+1) )
    #         test[x, y+1] += 1
    #         G.add_node( str(x+1)+','+str(y), pos = (x+1, y) )
    #         G.add_node( str(x)+','+str(y+1), pos = (x, y+1) )
    #         G.add_edge( str(x)+','+str(y), str(x+1)+','+str(y), weight = matrix[x+1, y] )
    #         G.add_edge( str(x)+','+str(y), str(x)+','+str(y+1), weight = matrix[x, y+1] )

    # # add the last node :
    # x = matrix.shape[0] - 1
    # y = matrix.shape[1] - 1
    # G.add_node( str(x)+','+str(y), pos = (x, y) )
    # labeldict[str(x)+','+str(y)] = matrix[x, y]
    # labeltest.append( str(x)+','+str(y) )
    # test[x, y] += 1
    # # add edges grom last row/column
    # y = matrix.shape[1] - 1
    # for x in range(matrix.shape[0] - 1):
    #     G.add_edge( str(x)+','+str(y), str(x+1)+','+str(y), weight = matrix[x+1, y] )

    # x = matrix.shape[0] - 1
    # for y in range(matrix.shape[1] - 1):
    #     G.add_edge( str(x)+','+str(y), str(x)+','+str(y+1), weight = matrix[x, y+1] )

    # print( len(np.where( test > 1 )[0]) )
    # print( len(labeldict) , matrix.shape[0]*matrix.shape[1], G.number_of_nodes() )
    # print(len(labeltest))

    path = nx.shortest_path(
        G,
        source="0,0",
        target=str(matrix.shape[0] - 1) + "," + str(matrix.shape[1] - 1),
        weight="weight",
    )
    summ = []
    for pos in path[1:]:
        summ.append(labeldict[pos])
    print(path)
    print(summ)
    print(sum(summ))

    # labels = [ item for item in labeltest ]
    # print(labeltest[0])
    # uniques, counts = np.unique(labels, return_counts=True)
    # doublons = np.where(counts>1)
    # for item in doublons:
    #     print( 'doublons : ', uniques[item] )
    # print(uniques)

    # pos=nx.get_node_attributes(G,'pos')
    # nx.draw(G,pos, labels=labeldict, with_labels = True)
    # labels = nx.get_edge_attributes(G,'weight')
    # nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    # plt.show()

    print("reminder : answer is between 435 and 485")


def solve_part_2(input_file):
    print("Solving puzzle part 2")
    open(input_file, "r").read().split("\n")


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed in {} milisecondes".format(1000 * (end - start)))
