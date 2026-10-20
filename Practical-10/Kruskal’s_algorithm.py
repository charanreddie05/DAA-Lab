# Kruskal's Algorithm

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


# User Input
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

for i in range(e):
    u = int(input("Enter source vertex: "))
    v = int(input("Enter destination vertex: "))
    w = int(input("Enter edge weight: "))

    edges.append((w, u, v))

# Sort edges by weight
edges.sort()

parent = list(range(n))
rank = [0] * n

mst = []
total_cost = 0

for w, u, v in edges:
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:
        mst.append((u, v, w))
        total_cost += w
        union(parent, rank, root_u, root_v)

        if len(mst) == n - 1:
            break

# Display result
if len(mst) == n - 1:
    print("\nEdges in Minimum Spanning Tree:")
    for u, v, w in mst:
        print(u, "-", v, ":", w)

    print("Minimum Cost =", total_cost)
else:
    print("Minimum Spanning Tree is not possible.")
    print("The graph is disconnected.")
