from collections import defaultdict

def kosaraju_scc(vertices, adj_list):
    def dfs(v, visited, stack):
        visited[v] = True
        for neighbor in adj_list[v]:
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)
        stack.append(v)

    def reverse_graph():
        rev_adj_list = defaultdict(list)
        for v in adj_list:
            for neighbor in adj_list[v]:
                rev_adj_list[neighbor].append(v)
        return rev_adj_list

    def dfs_reverse(v, visited, component):
        visited[v] = True
        component.append(v)
        for neighbor in rev_adj_list[v]:
            if not visited[neighbor]:
                dfs_reverse(neighbor, visited, component)
    
    # Step 1: DFS to fill stack
    stack = []
    visited = [False] * vertices
    for i in range(vertices):
        if not visited[i]:
            dfs(i, visited, stack)
    
    # Step 2: Reverse the graph
    rev_adj_list = reverse_graph()
    
    # Step 3: Pop from stack and perform DFS on reversed graph
    visited = [False] * vertices
    scc = []
    while stack:
        v = stack.pop()
        if not visited[v]:
            component = []
            dfs_reverse(v, visited, component)
            scc.append(component)
    
    return scc

# Example usage
vertices = 5
edges = [(1, 0), (0, 2), (2, 1), (0, 3), (3, 4)]
adj_list = defaultdict(list)
for u, v in edges:
    adj_list[u].append(v)

print("Strongly Connected Components:", kosaraju_scc(vertices, adj_list))
#Strongly Connected Components: [[4], [3], [0, 2, 1]]

