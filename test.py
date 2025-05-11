from collections import deque, defaultdict

class AuthorGraph:
    def __init__(self):
        # This will store the authors and their co-authors (edges)
        self.graph = defaultdict(set)
        
    def add_paper(self, paper, authors):
        # Connect all authors in a paper (undirected graph)
        for author in authors:
            for co_author in authors:
                if author != co_author:
                    self.graph[author].add(co_author)
                    
    def degrees_of_separation(self, start_author, target_author):
        # Perform BFS to find the shortest path between two authors
        if start_author == target_author:
            return [start_author]
        
        visited = set([start_author])
        queue = deque([(start_author, [start_author])])  # (current author, path to reach them)
        
        while queue:
            current_author, path = queue.popleft()
            
            for co_author in self.graph[current_author]:
                if co_author not in visited:
                    if co_author == target_author:
                        return path + [co_author]
                    visited.add(co_author)
                    queue.append((co_author, path + [co_author]))
        
        return None  # No connection found

# Example usage:
g = AuthorGraph()
g.add_paper('Paper1', ['Alice', 'Bob', 'Charlie'])
g.add_paper('Paper2', ['Bob', 'David'])
g.add_paper('Paper3', ['Charlie', 'David', 'Eve'])

result = g.degrees_of_separation('Alice', 'Eve')
print("Degrees of Separation:", result)
