from collections import defaultdict
from math import inf
from typing import Any
from heapq import heappush, heappop


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
            # choosing current node
            min_distance = inf
            min_index = inf
            for idx in unvisited:
                if distance[idx] < min_distance:
                    min_distance = distance[idx]
                    min_index = idx

            current_node = self.graph[nodes[min_index]]
            unvisited.remove(min_index)  # removing current node from unvisited

            for edge, weight in current_node.items():
                new_distance = weight + distance[min_index]  # combining the distance between two edges
                if new_distance < distance[dist_id := nodes.index(edge)]:
                    distance[dist_id] = new_distance
                    last[dist_id] = list(current_node.keys())[0]

        return distance

    def bfs_path(self, start_node: Any, end_node: Any) -> list[Any]:
        queue = [[start_node]]
        visited = set()

        while queue:
            path = queue.pop(0)
            last_node = path[-1]

            if last_node not in visited:
                visited.add(last_node)
                for adjacent_node in self.graph[last_node]:
                    new_path = list(path)
                    new_path.append(adjacent_node)
                    queue.append(new_path)

                    if new_path[-1] == end_node:
                        return new_path

        return []

    def dfs_path(self, start_node: Any, end_node: Any) -> list[Any]:
        stack = [[start_node]]
        visited = set()

        while stack:
            path = stack.pop()
            last_node = path[-1]

            if last_node not in visited:
                visited.add(last_node)
                for adjacent_node in self.graph[last_node]:
                    new_path = list(path)
                    new_path.append(adjacent_node)
                    stack.append(new_path)

                    if new_path[-1] == end_node:
                        return new_path

        return []

    def dijkstra_path(self, start_node: Any, end_node: Any) -> list[Any]:
        queue = [(0, [start_node])]
        visited = set()

        while queue:
            distance, path = heappop(queue)
            last_node = path[-1]

            if last_node not in visited:
                visited.add(last_node)

            for adjacent_node, adjacent_distance in self.graph[last_node].items():
                if adjacent_node not in visited:
                    new_path = list(path)
                    new_path.append(adjacent_node)
                    total_distance = distance + adjacent_distance
                    heappush(queue, (total_distance, new_path))

                    if new_path[-1] == end_node:
                        return new_path

        return []

    def bidirectional_search_path(self, start_node: Any, end_node: Any) -> list[Any]:
        """Bidirectional search of the graph."""
        queue_start = [[start_node]]
        queue_end = [[end_node]]
        visited = set()

        while queue_start and queue_end:
            path_start = queue_start.pop(0)
            path_end = queue_end.pop(0)
            node_start = path_start[-1]
            node_end = path_end[-1]
            adjacent_nodes_start = []
            adjacent_nodes_end = []

            if node_start not in visited:
                visited.add(node_start)

                for adjacent_node1 in self.graph[node_start]:
                    new_path = path_start + [adjacent_node1]
                    queue_start.append(new_path)
                    adjacent_nodes_start.append(adjacent_node1)

            if node_end not in visited:
                visited.add(node_end)

                for adjacent_node2 in self.graph[node_end]:
                    new_path = path_end + [adjacent_node2]
                    queue_end.append(new_path)
                    adjacent_nodes_end.append(adjacent_node2)

            if inter := set(adjacent_nodes_start).intersection(set(adjacent_nodes_end)):
                value = list(inter)[0]
                start_idx = adjacent_nodes_start.index(value)
                end_idx = adjacent_nodes_end.index(value)

                return queue_start.pop(start_idx)[:-1] + queue_end.pop(end_idx)[::-1]

        return []


if __name__ == "__main__":
    graph = Graph()
    graph.add_node('S')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node('E')
    graph.add_node('D')
    graph.add_node('F')
    graph.add_node('G')
    graph.add_node('H')
    graph.add_node('Z')

    graph.add_edge('S', 'B', 1)
    graph.add_edge('B', 'S', 1)
    graph.add_edge('S', 'C', 1)
    graph.add_edge('C', 'S', 1)
    graph.add_edge('B', 'E', 1)
    graph.add_edge('E', 'B', 1)
    graph.add_edge('B', 'D', 1)
    graph.add_edge('D', 'B', 1)
    graph.add_edge('C', 'E', 1)
    graph.add_edge('E', 'C', 1)
    graph.add_edge('E', 'F', 1)
    graph.add_edge('F', 'E', 1)
    graph.add_edge('E', 'G', 1)
    graph.add_edge('G', 'E', 1)
    graph.add_edge('D', 'G', 1)
    graph.add_edge('G', 'D', 1)
    graph.add_edge('D', 'H', 1)
    graph.add_edge('H', 'D', 1)
    graph.add_edge('F', 'Z', 1)
    graph.add_edge('Z', 'F', 1)
    graph.add_edge('G', 'Z', 1)
    graph.add_edge('Z', 'G', 1)
    graph.add_edge('H', 'Z', 1)
    graph.add_edge('Z', 'H', 1)

    print(graph.dfs_path('S', 'Z'))
