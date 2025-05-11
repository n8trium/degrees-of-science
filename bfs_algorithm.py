# Breadth-First Search (BFS) algorithm

from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, node, neighbour):  
        self.graph[node].append(neighbour)
        self.graph[neighbour].append(node)

    def nth_degree_nodes(self, node, n):
        visited = {node: 0}
        queue = deque([(node, 0)])

        nth_degree_nodes = []

        while queue:
            current_node, degree = queue.popleft()

            if degree == n:
                nth_degree_nodes.append(current_node)
            elif degree < n:
                for neighbour in self.graph[current_node]:
                    if neighbour not in visited:
                        visited[neighbour] = degree + 1
                        queue.append((neighbour, degree + 1))

        return nth_degree_nodes


g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('D', 'G')
g.add_edge('E', 'H')
g.add_edge('F', 'I')
g.add_edge('G', 'J')

print("4th degree nodes of A:", g.nth_degree_nodes('A', 4))  # ['J']
