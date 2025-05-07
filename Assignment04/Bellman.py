import csv
import os
from collections import defaultdict, deque
import sys

def build_adjacency_list(n, edges, weights):
    adj_list = defaultdict(list)
    for (u, v), w in zip(edges, weights):
        adj_list[u].append((v, w))  
    return adj_list

def bellman(n, adj_list, start):
    dist = [float('inf')] * n
    dist[start] = 0

    for _ in range(n-1):
        for u in range(n):
            for v, weight in adj_list[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
    
    for u in range(n):
        for v, weight in adj_list[u]:
            if dist[v] > dist[u] + weight:
                return [-1]  
    
    return [dist[i] if dist[i] != float('inf') else 100000 for i in range(n)]

def read_graph_from_csv(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
        n = int(lines[0])  
        edges = []
        weights = []

        for line in lines[1:-1]:  
            if ',' in line:
                u, v, w = map(int, line.strip().split(','))
                edges.append((u, v))
                weights.append(w)
        
        start_vertex = int(lines[-1])  
                
        return n, start_vertex, edges, weights

if __name__ == "__main__":
    file_path = sys.argv[1] 
    n, start_vertex, edges, weights = read_graph_from_csv(file_path)
    
    adj_list = build_adjacency_list(n, edges, weights)
    result = bellman(n, adj_list, start_vertex)
    
    print(','.join(map(str, result)))
