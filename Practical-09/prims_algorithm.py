import sys

# Number of vertices
n = int(input("Enter number of vertices: "))

# Enter adjacency matrix
print("Enter the adjacency matrix:")
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

selected = [False] * n
selected[0] = True

print("\nEdges in Minimum Spanning Tree:")

edges = 0
total_cost = 0

while edges < n - 1:
    minimum = sys.maxsize
    x = 0
    y = 0

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(x, "--", y, "=", graph[x][y])

    total_cost += graph[x][y]
    selected[y] = True
    edges += 1

print("Minimum Cost =", total_cost)
