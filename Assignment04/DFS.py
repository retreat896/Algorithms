import csv
import os
from collections import defaultdict, deque
import sys

def build_adjacency_list(n, edges):
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list

def dfs(n, adj_list, start):
    visited = [False] * n
    result = []
    queue = deque([start])
    visited[start] = True
    
    while queue:
        return
    return result

def read_graph_from_csv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        n = int(lines[0])  
        edges = []

        for line in lines[1:-1]:
            if ',' in line:
                u, v = map(int, line.strip().split(','))
                edges.append((u, v))
        start_vertex = int(lines[-1])  
        return n, start_vertex, edges

if __name__ == "__main__":
    file_path = sys.argv[1] 
    n, start_vertex, edges = read_graph_from_csv(file_path)
    
    adj_list = build_adjacency_list(n, edges)
    result = dfs(n, adj_list, start_vertex)
    
    print(f"{result}")
