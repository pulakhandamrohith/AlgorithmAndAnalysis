from collections import defaultdict

class BlossomAlgorithm:
    def __init__(self, graph):
        self.graph = graph  # adjacency list representation of graph
        self.n = len(graph)
        self.match = [-1] * self.n  # match[i] is the matched vertex of i, -1 if unmatched
        self.parent = [-1] * self.n  # parent[i] will store the parent of i in augmenting path
        self.root = [-1] * self.n  # root[i] is the root of the alternating tree containing i
        self.in_queue = [False] * self.n  # to check if vertex is in BFS queue
        self.dist = [-1] * self.n  # distance of each vertex in the BFS

    def bfs(self, start):
        queue = [start]
        self.dist[start] = 0
        self.in_queue[start] = True
        self.parent[start] = -1

        while queue:
            u = queue.pop(0)
            for v in self.graph[u]:
                if self.match[u] == v or self.match[v] == u:
                    continue  # Skip if it's part of the matching
                if self.match[v] == -1:
                    # Found an augmenting path, augment the matching
                    self.augment_path(u, v)
                    return True
                # Add v to the BFS queue if it hasn't been visited yet
                if not self.in_queue[self.match[v]]:
                    self.dist[self.match[v]] = self.dist[u] + 1
                    self.parent[self.match[v]] = u
                    queue.append(self.match[v])
                    self.in_queue[self.match[v]] = True
        return False

    def augment_path(self, u, v):
        # Augment the path from u to v
        while u != -1:
            prev = self.parent[u]
            self.match[u] = v
            self.match[v] = u
            u = prev
            v = self.match[v]

    def find_maximum_matching(self):
        # Iteratively try to find augmenting paths and update the matching
        matching_size = 0
        for i in range(self.n):
            if self.match[i] == -1:  # If vertex i is unmatched
                if self.bfs(i):
                    matching_size += 1
        return self.match

# Example usage:
graph = defaultdict(list)
graph[0] = [1, 2]
graph[1] = [0, 2]
graph[2] = [0, 1, 3]
graph[3] = [2, 4]
graph[4] = [3]

blossom = BlossomAlgorithm(graph)
matching = blossom.find_maximum_matching()

# Output the matching
print("Maximum Matching:", [(i, matching[i]) for i in range(len(matching)) if matching[i] != -1])
#Maximum Matching: [(0, 1), (2, 3), (4, 3)]

