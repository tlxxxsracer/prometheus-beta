import pytest
from src.dijkstra_shortest_path import dijkstra_shortest_path

def test_basic_graph():
    # Simple graph with clear shortest path
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'D')
    assert path == ['A', 'C', 'B', 'D']
    assert distance == 6  # 2 (A to C) + 1 (C to B) + 3 (B to D)

def test_single_node_path():
    # Path from a node to itself
    graph = {
        'A': {},
        'B': {}
    }
    graph['A'][('A')] = 0
    path, distance = dijkstra_shortest_path(graph, 'A', 'A')
    assert path == ['A']
    assert distance == 0

def test_no_direct_path():
    # More complex graph requiring multiple hops
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'D': 3},
        'C': {'D': 2},
        'D': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'D')
    assert path == ['A', 'B', 'D']
    assert distance == 4  # 1 (A to B) + 3 (B to D)

def test_multiple_paths():
    # Graph with multiple possible paths
    graph = {
        'A': {'B': 1, 'C': 3},
        'B': {'D': 2},
        'C': {'D': 1},
        'D': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'D')
    assert path == ['A', 'B', 'D']
    assert distance == 3  # 1 (A to B) + 2 (B to D)

def test_nonexistent_start_node():
    graph = {
        'A': {'B': 1},
        'B': {}
    }
    with pytest.raises(ValueError, match="Start node 'C' not found in graph"):
        dijkstra_shortest_path(graph, 'C', 'B')

def test_nonexistent_end_node():
    graph = {
        'A': {'B': 1},
        'B': {}
    }
    with pytest.raises(ValueError, match="End node 'C' not found in graph"):
        dijkstra_shortest_path(graph, 'A', 'C')

def test_no_path_between_nodes():
    graph = {
        'A': {},
        'B': {},
        'C': {}
    }
    with pytest.raises(ValueError, match="No path exists between A and B"):
        dijkstra_shortest_path(graph, 'A', 'B')

def test_complex_graph():
    # More complex graph with multiple connections
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3, 'E': 1},
        'C': {'B': 1, 'D': 5},
        'D': {'E': 2},
        'E': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'E')
    assert path == ['A', 'C', 'B', 'E']
    assert distance == 4  # 2 (A to C) + 1 (C to B) + 1 (B to E)