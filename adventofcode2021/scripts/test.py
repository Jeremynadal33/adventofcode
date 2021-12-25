import sys
import networkx as nx
import numpy as np



data = np.genfromtxt(sys.argv[1], delimiter=1, dtype=int)    
G = nx.DiGraph()

for ix, iy in np.ndindex(data.shape):
    if ix > 0: 
        G.add_edge((ix - 1, iy), (ix, iy), weight = data[(ix, iy)])

    if ix < data.shape[0] - 1:
        G.add_edge((ix + 1, iy), (ix, iy), weight = data[(ix, iy)])

    if iy > 0:
        G.add_edge((ix, iy - 1), (ix, iy), weight = data[(ix, iy)])

    if iy < data.shape[1] -1:
        G.add_edge((ix, iy + 1), (ix, iy), weight = data[(ix, iy)])



print(nx.dijkstra_path_length(G, (0, 0), (data.shape[0] - 1, data.shape[1] -1)))