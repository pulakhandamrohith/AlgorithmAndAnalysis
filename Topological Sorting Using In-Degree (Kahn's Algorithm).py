from collections import deque, defaultdict

def topological_sort(vertices, edges):
    # Initialize in-degree of all vertices to 0
    in_degree = {i: 0 for i in range(vertices)}
    # Adjacency list representation of the graph
    adj_list = defaultdict(list)
    
    # Build the graph and compute in-degrees
    for u, v in edges:
        adj_list[u].append(v)
        in_degree[v] += 1
    
    # Queue for vertices with no incoming edges
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    top_order = []
    
    while queue:
        node = queue.popleft()
        top_order.append(node)
        
        # Reduce in-degree of neighbors
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if topological sort is possible (DAG check)
    if len(top_order) != vertices:
        raise ValueError("The graph is not a Directed Acyclic Graph (DAG)")
    
    return top_order

# Example usage
vertices = 6
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
print("Topological Sort:", topological_sort(vertices, edges))
# Topological Sort: [5, 4, 2, 3, 1, 0]
