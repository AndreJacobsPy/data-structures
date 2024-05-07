from graph.directed import Graph


def test_simple_bfs():
    directed_graph = Graph()

    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    for node in nodes:
        directed_graph.add_node(node)

    directed_graph.add_edge('A', 'B', 1)
    directed_graph.add_edge('B', 'C', 1)
    directed_graph.add_edge('B', 'D', 1)
    directed_graph.add_edge('C', 'E', 1)
    directed_graph.add_edge('D', 'E', 1)
    directed_graph.add_edge('E', 'F', 1)

    order = directed_graph.bfs('A')
    assert order == ['A', 'B', 'C', 'D', 'E', 'F']


def test_simple_bfs_find():
    directed_graph = Graph()
    nodes = ['A', 'B', 'C', 'D']

    for node in nodes:
        directed_graph.add_node(node)

    directed_graph.add_edge("A", "B", 2)
    directed_graph.add_edge("B", "C", 2)
    directed_graph.add_edge("C", "D", 3)
    directed_graph.add_edge("A", "C", 1)

    assert directed_graph.bfs_path("A", "D") == ["A", "C", "D"]
