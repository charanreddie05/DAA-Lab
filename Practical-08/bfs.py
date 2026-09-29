# BFS Traversal

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        vertex = queue.popleft()

        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# User Input
n = int(input("Enter number of vertices: "))

graph = {}

for i in range(n):
    graph[i] = []

e = int(input("Enter number of edges: "))

for i in range(e):
    u = int(input("Enter first vertex: "))
    v = int(input("Enter second vertex: "))

    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting vertex: "))

print("BFS Traversal:")
bfs(graph, start)
