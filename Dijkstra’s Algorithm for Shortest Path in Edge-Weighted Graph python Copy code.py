import heapq

def dijkstra(vertices, adj_list, start):
    # Initialize distances and priority queue
    distances = {i: float('inf') for i in range(vertices)}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_distance > distances[current_vertex]:
            continue
        
        # Explore neighbors
        for neighbor, weight in adj_list[current_vertex]:
            distance = current_distance + weight
            
            # Only update if we find a shorter path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example usage
vertices = 5
adj_list = {
    0: [(1, 9), (2, 6), (3, 5), (4, 3)],
    1: [(0, 9), (2, 2)],
    2: [(0, 6), (1, 2), (3, 4)],
    3: [(0, 5), (2, 4)],
    4: [(0, 3)]
}
start = 0
print(dijkstra(vertices, adj_list, start))

#Shortest Path from Node 0: {0: 0, 1: 8, 2: 6, 3: 5, 4: 3}

