import logging
import os

logging = logging.getLogger(__name__)
logging.root.setLevel(os.environ.get("LOG_LEVEL", "INFO"))

class Graph:
    """A simple directed graph implementation using adjacency list representation."""

    def __init__(self):
        self.graph = {}

    @property
    def nodes(self):
        """Return all nodes in the graph."""
        return list(self.graph.keys())
    
    @property
    def edges(self):
        """Return all edges in the graph as (node1, node2) tuples."""
        edge_list = []
        for node1 in self.graph:
            for node2 in self.graph[node1]:
                edge_list.append((node1, node2))
        return edge_list

    def add_node(self, node):
        """Add a node to the graph."""
        if node not in self.graph:
            self.graph[node] = {}

    def add_edge(self, node1, node2, weight=1):
        """Add a directed edge from node1 to node2 with a given weight."""
        self.add_node(node1)
        self.add_node(node2)
        self.graph[node1][node2] = weight
    
    def remove_edge(self, node1, node2):
        """Remove the directed edge from node1 to node2."""
        if node1 in self.graph and node2 in self.graph[node1]:
            del self.graph[node1][node2]
    
    def remove_node(self, node):
        """Remove a node and all associated edges."""
        if node in self.graph:
            del self.graph[node]
        for n in self.graph:
            if node in self.graph[n]:
                del self.graph[n][node]

    def get_neighbors(self, node):
        """Get all neighbors of a given node."""
        try:
            return self.graph[node]
        except KeyError:
            raise ValueError(f"Node {node} not found in the graph.")
    
    def dikjstra(self, start_node):
        """Dijkstra's algorithm to find the shortest path from start_node to all other nodes."""
        raise NotImplementedError("Dijkstra's algorithm is not implemented yet.")

    def _BFS_dummy(self, start_node):
        """
            Breadth-First Search traversal from start_node using a queue.
        """
        raise NotImplementedError("BFS traversal is not implemented yet.")
    
    def _BFS_recursive(self, start_node):
        """Recursive Breadth-First Search traversal from start_node using recursion.
        https://www.youtube.com/watch?v=cS-198wtfj0"""
        raise NotImplementedError("Recursive BFS traversal is not implemented yet.")
    
    def BFS(self, start_node):
        """
            Iterative Breadth-First Search traversal from start_node
            Best for shortest path in unweighted graphs, look for all nodes layer by layer.
        """
        return self._BFS_dummy(start_node)
    
    def _DFS_dummy(self, start_node):
        """
            Depth-First Search traversal from start_node using a stack.
        """
        stack = [start_node]
        visited = set()

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            for neighbor in self.get_neighbors(node).keys():
                if neighbor not in visited and neighbor not in stack:
                    stack.append(neighbor)
                    logging.debug(f"For node {node}, stack updated: {stack}")
            visited.add(node)
        return visited

    def _DFS_recursive(self, start_node):
        """Recursive Depth-First Search traversal from start_node using recursion.
        https://www.youtube.com/watch?v=7fujbpJ0LB4"""
        raise NotImplementedError("Recursive DFS traversal is not implemented yet.")
    
    def DFS(self, start_node):
        """
            Iterative Depth-First Search traversal from start_node.
            Best for pathfinding in mazes, exploring all possibilities, backtracking.
        """
        if start_node not in self.graph:
            raise ValueError(f"Node {start_node} not found in the graph.")
        return self._DFS_dummy(start_node)


    def connected_components(self):
        """
            Find all connected components in the graph.
            A connected component is a subgraph where any two nodes are connected to each other by paths.
        """
        visited = set()
        components = []

        for node in self.nodes:
            if node not in visited:
                component = self.DFS(node)
                components.append(component)
                visited.update(component)
        
        return components
    
    def is_connected(self):
        """
            Check if the graph is fully connected.
            A graph is connected if there is a path between every pair of nodes.
        """
        if not self.nodes:
            return True  # An empty graph is considered connected

        # Take an arbitrary starting node
        start_node = self.nodes[0]
        visited = self.DFS(start_node)

        return len(visited) == len(self.nodes)