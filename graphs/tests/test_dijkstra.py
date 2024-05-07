from graph.directed import Graph


def test_simple_dijkstra():
    graph = Graph()

    nodes = ['A', 'B', 'C', 'D', 'E']
    for node in nodes:
        graph.add_node(node)

    graph.add_edge('A', 'B', 2)
    graph.add_edge('A', 'C', 1)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 1)
    graph.add_edge('C', 'D', 3)
    graph.add_edge('C', 'E', 2)
    graph.add_edge('D', 'E', 2)

    distances = graph.dijkstra('A')
    assert distances == [0, 2, 1, 3, 3]


def test_simple_dijkstra_find():
    directed_graph = Graph()
    nodes = ['A', 'B', 'C', 'D']

    for node in nodes:
        directed_graph.add_node(node)

    directed_graph.add_edge("A", "B", 2)
    directed_graph.add_edge("B", "C", 2)
    directed_graph.add_edge("C", "D", 3)
    directed_graph.add_edge("A", "C", 1)

    assert directed_graph.dijkstra_path("A", "D") == ["A", "C", "D"]


def test_complex_dijkstra_path():
    directed_graph = Graph()
    nodes = ['A', 'B', 'C', 'D', 'E']

    for node in nodes:
        directed_graph.add_node(node)

    directed_graph.add_edge("A", "B", 1)
    directed_graph.add_edge("B", "C", 1)
    directed_graph.add_edge("C", "D", 2)
    directed_graph.add_edge("A", "C", 3)
    directed_graph.add_edge("D", "E", 1)

    assert directed_graph.dijkstra_path("A", "E") == ["A", "B", "C", "D", "E"]
