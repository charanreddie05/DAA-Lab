def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


# User Input
n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

# Sort the array
merge_sort(arr)

# Display the sorted array
print("Sorted Array:")
for num in arr:
    print(num, end=" ")
