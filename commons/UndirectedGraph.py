import logging
import os

from commons.Graph import Graph

logging = logging.getLogger(__name__)
logging.root.setLevel(os.environ.get("LOG_LEVEL", "INFO"))

class UndirectedGraph(Graph):
    """A simple undirected graph implementation using adjacency list representation."""

    def __init__(self):
        super().__init__()

    def add_edge(self, node1, node2, weight=1):
        """Add a directed edge from node1 to node2 with a given weight."""
        self.add_node(node1)
        self.add_node(node2)
        self.graph[node1][node2] = weight
        self.graph[node2][node1] = weight
