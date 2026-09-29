# DFS Traversal

def dfs(graph, vertex, visited):
    visited.add(vertex)

    print(vertex, end=" ")

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


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

visited = set()

start = int(input("Enter starting vertex: "))

print("DFS Traversal:")
dfs(graph, start, visited)
