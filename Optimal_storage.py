def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def optimal_storage_on_tape(program_lengths):
    # Step 1: Sort program lengths using bubble sort
    sorted_lengths = bubble_sort(program_lengths[:])

    # Step 2: Compute retrieval times
    retrieval_times = []
    cumulative_sum = 0
    for length in sorted_lengths:
        cumulative_sum += length
        retrieval_times.append(cumulative_sum)

    # Step 3: Compute Mean Retrieval Time (MRT)
    mrt = sum(retrieval_times) / len(retrieval_times)

    return sorted_lengths, retrieval_times, mrt


# Taking input from user
n = int(input("Enter number of programs: "))
programs = []

print("Enter the lengths of programs:")
for i in range(n):
    length = int(input(f"Program {i+1} length: "))
    programs.append(length)

sorted_programs, retrieval_times, mrt = optimal_storage_on_tape(programs)

print("\nOriginal Programs:", programs)
print("Sorted Programs (Optimal Order):", sorted_programs)
print("Retrieval Times:", retrieval_times)
print("Mean Retrieval Time (MRT):", mrt)


#output
Enter number of programs: 5
Enter the lengths of programs:
Program 1 length: 10
Program 2 length: 5
Program 3 length: 3
Program 4 length: 2
Program 5 length: 8

Original Programs: [10, 5, 3, 2, 8]
Sorted Programs (Optimal Order): [2, 3, 5, 8, 10]
Retrieval Times: [2, 5, 10, 18, 28]
Mean Retrieval Time (MRT): 12.6
