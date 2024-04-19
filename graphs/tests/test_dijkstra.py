from graphs.directed import Graph


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
