# ----------------------------
# Hash Function Implementation
# ----------------------------

# Custom hash function
# This takes a string 'key' and sums up the ASCII values of each character.
# Then it returns the remainder when divided by table_size (modulus).
def custom_hash(key, table_size):
    hash_value = 0
    for c in key:
        hash_value += ord(c)  # ord() gives ASCII value of the character
    return hash_value % table_size


# Insert function with linear probing
# If the computed index is already occupied, move to the next index
# until an empty slot is found (circular search using % operator).
def insert(key, table_size, hash_table):
    index = custom_hash(key, table_size)  # initial hash index
    start_index = index  # store the starting index to detect full table

    while hash_table[index] is not None:
        index = (index + 1) % table_size  # move to the next index
        if index == start_index:  # if we have looped back to start, table is full
            return  # ignore insertion if table is full

    hash_table[index] = key  # insert the key


# Display function
# Prints the contents of the hash table in index order.
def display_table(hash_table):
    print("\nHash Table:")
    for i in range(len(hash_table)):
        print(f"Index {i}: {hash_table[i] if hash_table[i] is not None else 'null'}")


# Main program execution
if __name__ == "__main__":
    # Step 1: Get table size from user
    table_size = int(input("Enter table size: "))

    # Step 2: Get keys from user in one line (space-separated)
    keys = input("Enter keys separated by space: ").split()

    # Step 3: Create an empty hash table
    hash_table = [None] * table_size

    # Step 4: Insert each key into the hash table
    for key in keys:
        insert(key, table_size, hash_table)

    # Step 5: Display the final hash table
    display_table(hash_table)


# Enter table size: 5
# Enter keys separated by space: apple banana cherry date

# Hash Table:
# Index 0: apple
# Index 1: cherry
# Index 2: date
# Index 3: null
# Index 4: banana



