
# Travelling Salesman Problem

from itertools import permutations

n = int(input("Enter number of cities: "))

print("Enter the cost matrix:")
cost = []

for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

start = 0
cities = list(range(n))
cities.remove(start)

min_cost = float('inf')
best_path = []

for p in permutations(cities):
    path = [start] + list(p) + [start]
    total_cost = 0

    for i in range(len(path) - 1):
        total_cost += cost[path[i]][path[i + 1]]

    if total_cost < min_cost:
        min_cost = total_cost
        best_path = path

print("\nMinimum Cost:", min_cost)
print("Best Path:", end=" ")

for city in best_path:
    print(city, end=" ")
