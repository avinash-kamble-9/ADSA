# Merge Sort Implementation in Python (with user input)

# Function to merge two sorted subarrays
def merge(arr, left, mid, right):
    # Create temp arrays
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]

    # Indexes for temp arrays
    i = 0  # Left array index
    j = 0  # Right array index
    k = left  # Merged array index

    # Merge the temp arrays back into arr[left:right+1]
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy any remaining elements of L[]
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy any remaining elements of R[]
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


# Recursive function to sort the array
def merge_sort(arr, left, right):
    if left < right:
        # Find the middle point
        mid = (left + right) // 2

        # Sort first half
        merge_sort(arr, left, mid)

        # Sort second half
        merge_sort(arr, mid + 1, right)

        # Merge the sorted halves
        merge(arr, left, mid, right)


# --- Main Program ---
# Take number of elements from user
n = int(input("Enter the number of elements: "))

# Take array elements from user
arr = []
print("Enter the elements:")
for _ in range(n):
    arr.append(int(input()))

# Display original array
print("Original array:", arr)

# Call merge sort function
merge_sort(arr, 0, n - 1)

# Display sorted array
print("Sorted array:", arr)




#Enter the number of elements: 5
#Enter the elements:
#38
#27
#43
#3
#9
#Original array: [38, 27, 43, 3, 9]
#Sorted array: [3, 9, 27, 38, 43]

