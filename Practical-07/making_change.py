coins = list(map(int, input("Enter coin denominations separated by space: ").split()))

amount = int(input("Enter the amount: "))

dp = [float('inf')] * (amount + 1)

dp[0] = 0

for i in range(1, amount + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[amount] == float('inf'):
    print("Change cannot be made.")
else:
    print("Minimum number of coins required:", dp[amount])
