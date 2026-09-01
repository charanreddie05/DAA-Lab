# Chain Matrix Multiplication using Dynamic Programming

def matrix_chain_order(p, n):
    # m[i][j] stores minimum multiplication cost
    m = [[0] * (n + 1) for _ in range(n + 1)]

    # s[i][j] stores the position where the chain is split
    s = [[0] * (n + 1) for _ in range(n + 1)]

    # length is the chain length
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = float('inf')

            for k in range(i, j):
                cost = (
                    m[i][k]
                    + m[k + 1][j]
                    + p[i - 1] * p[k] * p[j]
                )

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


# Function to print optimal parenthesization
def print_parenthesis(s, i, j):
    if i == j:
        return f"A{i}"

    k = s[i][j]

    left = print_parenthesis(s, i, k)
    right = print_parenthesis(s, k + 1, j)

    return f"({left} x {right})"


# User input
n = int(input("Enter number of matrices: "))

print("Enter the dimensions of matrices:")
print("Example: For A1(10x20), A2(20x30), A3(30x40), enter: 10 20 30 40")

p = list(map(int, input().split()))

# Validate input
if len(p) != n + 1:
    print("Invalid input! You must enter", n + 1, "dimensions.")
else:
    m, s = matrix_chain_order(p, n)

    print("\nMinimum number of scalar multiplications:", m[1][n])

    print("Optimal Parenthesization:", print_parenthesis(s, 1, n))

    # Display DP table
    print("\nDP Cost Table:")

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j < i:
                print("-", end="\t")
            else:
                print(m[i][j], end="\t")
        print()
