import pytest
from commons.Graph import Graph


@pytest.fixture
def undirected_tree_graph():
    """
    Tree graph (no cycle):
         A
        / \
       B   C
      / \   \
     D   F   E
    """
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'F')
    graph.add_edge('C', 'E')
    return graph


@pytest.fixture
def undirected_cycle_graph():
    """
    Graph with multiple cycles (simulated undirected):
    A-B-D-F
    |\|X|/|
    | C-E |
    \-----/
    """
    graph = Graph()
    # Connexions de A
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'A')
    graph.add_edge('C', 'A')
    
    # Connexions de B
    graph.add_edge('B', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'B')
    graph.add_edge('D', 'B')
    graph.add_edge('E', 'B')
    
    # Connexions de C
    graph.add_edge('C', 'E')
    graph.add_edge('E', 'C')
    
    # Connexions de D
    graph.add_edge('D', 'E')
    graph.add_edge('D', 'F')
    graph.add_edge('E', 'D')
    graph.add_edge('F', 'D')
    
    # Connexions de E
    graph.add_edge('E', 'F')
    graph.add_edge('F', 'E')
    
    return graph


@pytest.fixture
def partially_connected_graph():
    """
    Partially connected graph:
    A -> B -> C
    
    D -> E
    
    F (isolated node)
    (three separate components)
    """
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('D', 'E')
    graph.add_node('F')
    return graph


@pytest.fixture
def sparse_directed_graph():
    """
    Sparse directed graph with 20 nodes (0-19) and few connections:
    0 -> 19, 7
    2 -> 13, 8, 18
    7 -> 19
    9 -> 12
    11 -> 16
    14 -> 19
    17 -> 18
    (many isolated or terminal nodes)
    """
    graph = Graph()
    # Create the graph structure from the dictionary
    graph_dict = {
        0: {19: 1, 7: 1}, 1: {}, 2: {13: 1, 8: 1, 18: 1}, 3: {}, 4: {}, 
        5: {}, 6: {}, 7: {19: 1}, 8: {}, 9: {12: 1}, 10: {}, 11: {16: 1}, 
        12: {}, 13: {}, 14: {19: 1}, 15: {}, 16: {}, 17: {18: 1}, 18: {}, 19: {}
    }
    
    for node, neighbors in graph_dict.items():
        graph.add_node(node)
        for neighbor, weight in neighbors.items():
            graph.add_edge(node, neighbor, weight)
    
    return graph


def test__DFS_dummy_undirected_tree(undirected_tree_graph):
    result = undirected_tree_graph._DFS_dummy('A')
    assert set(result) == {'A', 'B', 'C', 'D', 'E', 'F'}

def test__DFS_dummy_undirected_cycle(undirected_cycle_graph):
    result = undirected_cycle_graph._DFS_dummy('A')
    expected_nodes = {'A', 'B', 'C', 'D', 'E', 'F'}
    assert set(result) == expected_nodes

def test__DFS_dummy_partially_connected(partially_connected_graph):
    result = partially_connected_graph._DFS_dummy('A')
    assert set(result) == {'A', 'B', 'C'}

###
def test_connected_components_partially_connected(partially_connected_graph):
    result = partially_connected_graph.connected_components()
    expected_components = [{'A', 'B', 'C'}, {'D', 'E'}, {'F'}]
    assert all(any(comp == set(expected) for comp in result) for expected in expected_components)

def test_connected_components_undirected_tree(undirected_tree_graph):
    result = undirected_tree_graph.connected_components()
    assert len(result) == 1
    assert set(result[0]) == {'A', 'B', 'C', 'D', 'E', 'F'}

def test_connected_components_undirected_cycle(undirected_cycle_graph):
    result = undirected_cycle_graph.connected_components()
    assert len(result) == 1
    assert set(result[0]) == {'A', 'B', 'C', 'D', 'E', 'F'}

def test_connected_components_sparse_directed(sparse_directed_graph):
    result = sparse_directed_graph.connected_components()
    expected_components = [
        {0, 7, 19},
        {1},
        {2, 8, 13, 18},
        {3},
        {4},
        {5},
        {6},
        {9, 12},
        {10},
        {11, 16},
        {14, 19},
        {15},
        {17, 18}
    ]
    assert len(result) == len(expected_components)
    assert all(any(comp == expected for comp in result) for expected in expected_components)