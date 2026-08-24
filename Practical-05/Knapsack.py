n = int(input("Enter the number of items: "))

weights = []
values = []

for i in range(n):
    w = int(input(f"Enter weight of item {i + 1}: "))
    v = int(input(f"Enter value of item {i + 1}: "))

    weights.append(w)
    values.append(v)

capacity = int(input("Enter the capacity of the knapsack: "))

# Create DP table
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

# Fill the DP table
for i in range(1, n + 1):
    for w in range(1, capacity + 1):

        # If item can fit in the knapsack
        if weights[i - 1] <= w:
            dp[i][w] = max(
                values[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

# Maximum value
print("\nMaximum value:", dp[n][capacity])

# Find selected items
w = capacity
selected_items = []

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected_items.append(i)
        w -= weights[i - 1]

selected_items.reverse()

print("Selected items:", selected_items)
print("Total weight:", sum(weights[i - 1] for i in selected_items))
print("Total value:", sum(values[i - 1] for i in selected_items))
