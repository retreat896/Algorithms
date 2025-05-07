import csv
import os
from collections import defaultdict, deque
import sys

def build_times_graph(n, times):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    return graph

def dijkstra(n, adj_list, start):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    visited = set()
    queue = [(0, start)]
    
    while queue:
        curr_dist, curr = min(queue)
        queue.remove((curr_dist, curr))
        
        if curr in visited:
            continue
            
        visited.add(curr)
        
        for neighbor, weight in adj_list[curr]:
            distance = curr_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                queue.append((distance, neighbor))
    
    max_time = max(distances[1:n+1])  
    return max_time if max_time != float('inf') else -1

def read_graph_from_csv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())  
        edges = []
        
        for line in lines[1:-1]:
            if ',' in line:
                u, v, w = map(int, line.strip().split(','))
                edges.append((u, v, w))  
                
        start_vertex = int(lines[-1].strip())  
        return n, start_vertex, edges

if __name__ == "__main__":
    file_path = sys.argv[1] 
    n, start_vertex, edges = read_graph_from_csv(file_path)
    
    times_list = build_times_graph(n, edges)
    result = dijkstra(n, times_list, start_vertex)
    
    print(f"{result}")
