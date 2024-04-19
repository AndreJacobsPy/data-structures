from collections import defaultdict
from math import inf
from typing import Any


class Graph:
    """This implementation of a directed graph represented as an adjacency list."""
    def __init__(self):
        self.graph = defaultdict(dict)

    def __repr__(self) -> str:
        return str(self.graph)

    def add_node(self, value: Any) -> None:
        self.graph[value] = {}

    def add_edge(self, node1: Any, node2: Any, distance: int | float) -> None:
        assert node1 and node2 in self.graph
        self.graph[node1] |= {node2: distance}

    def bfs(self, start_node: Any) -> list[Any]:
        """Breadth first search of the graph."""
        visited = set()
        queue = [start_node]  # using a queue makes this bfs
        result = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)  # keeping track of the nodes that were already visited
                result.append(node)  # nodes which are returned
                queue.extend(self.graph[node].keys())  # adding nodes at same level

        return result

    def dfs(self, start_node: Any) -> list[Any]:
        """Depth first search of the graph."""
        visited = set()
        stack = [start_node]  # using a stack makes this dfs
        result = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)  # keeping track of the nodes that were already visited
                result.append(node)  # nodes which are returned
                stack.extend(self.graph[node].keys())  # adding nodes at same level

        return result

    def dijkstra(self, start_node: Any) -> list[Any]:
        """Dijkstra's algorithm for finding the shortest paths from start node to all other nodes."""
        nodes = self.bfs(start_node)
        distance: list[int | float] = [inf for _ in nodes]
        last: list[Any] = [-1 for _ in nodes]
        unvisited: set[int] = set([i for i in range(len(nodes))])
        distance[nodes.index(start_node)] = 0

        while unvisited:
            min_distance = inf
            min_index = inf
            for idx in unvisited:
                if distance[idx] < min_distance:
                    min_distance = distance[idx]
                    min_index = idx

            current_node = self.graph[nodes[min_index]]
            unvisited.remove(min_index)

            for edge, weight in current_node.items():
                new_distance = weight + distance[min_index]  # combining the distance between two edges
                if new_distance < distance[dist_id := nodes.index(edge)]:
                    distance[dist_id] = new_distance
                    last[dist_id] = list(current_node.keys())[0]

        return distance


if __name__ == "__main__":
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")
    graph.add_edge("A", "B", 5)
    graph.add_edge("A", "C", 3)
    graph.add_edge("B", "D", 8)
    graph.add_edge("C", "E", 12)
    print(graph)

    print(graph.bfs("A"))
    print(graph.dfs("A"))
    print(graph.dijkstra("A"))
