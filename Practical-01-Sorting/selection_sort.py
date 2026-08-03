def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# User Input
n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

# Sort the array
selection_sort(arr)

# Display the sorted array
print("Sorted Array:")
for num in arr:
    print(num, end=" ")
