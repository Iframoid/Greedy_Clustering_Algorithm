#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Syeda Ifra Moid
Description: Greedy Clustering Algorithm.
"""


# Function to perform Kruskal's algorithm for single link k-clustering



# WRITE YOUR CODE HERE

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


def greedy_clustering_kruskal(distance_matrix, k):
    n = len(distance_matrix)

    if k > n or k < 1:
        print("Invalid number of clusters. Returning each node as its own cluster.")
        return [[i] for i in range(n)]  # Each node is its own cluster if k is invalid

    edges = [(distance_matrix[i][j], i, j) for i in range(n) for j in range(i + 1, n)]
    edges.sort()  # Sort edges by weight in O(n log n)

    uf = UnionFind(n)
    clusters = n
    selected_edges = []

    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            if clusters == k:
                break
            uf.union(u, v)
            selected_edges.append((u, v))
            clusters -= 1

    cluster_map = {uf.find(i): [] for i in range(n)}
    for i in range(n):
        cluster_map[uf.find(i)].append(i)

    return list(cluster_map.values())


distance_matrix = [
    [0, 38, 17, 28, 88, 59, 13],
    [38, 0, 52, 49, 83, 91, 59],
    [17, 52, 0, 46, 34, 77, 80],
    [28, 49, 46, 0, 5, 53, 62],
    [88, 83, 34, 5, 0, 43, 33],
    [59, 91, 77, 53, 43, 0, 27],
    [13, 59, 80, 62, 33, 27, 0]
]

# Set k=2 for number of clusters
k = 2
clusters = greedy_clustering_kruskal(distance_matrix, k)

# Print the resulting clusters
print("Resulting Clusters:", clusters)