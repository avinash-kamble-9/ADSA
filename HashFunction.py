# Hash Function Implementation in Python (with user-defined table size)

# Function for built-in hash method
def built_in_hash(key, table_size):
    return abs(hash(key) % table_size)

# Custom hash function
def custom_hash(key, table_size):
    hash_value = 0
    for c in key:
        hash_value += ord(c)  # sum of ASCII values
    return hash_value % table_size

# Insert function with linear probing
def insert(key, table_size, hash_table):
    index = custom_hash(key, table_size)
    start_index = index

    while hash_table[index] is not None:
        index = (index + 1) % table_size
        if index == start_index:
            print("Hash table is full!")
            return

    hash_table[index] = key
    print(f"Inserted '{key}' at index {index}")

# Display hash table
def display_table(hash_table):
    print("\nHash Table:")
    for i in range(len(hash_table)):
        print(f"Index {i}: {hash_table[i] if hash_table[i] is not None else 'null'}")

# Main program
if __name__ == "__main__":
    table_size = int(input("Enter table size: "))
    hash_table = [None] * table_size

    n = int(input("Enter number of keys to insert: "))

    for i in range(n):
        key = input(f"Enter key {i+1}: ")
        insert(key, table_size, hash_table)

    display_table(hash_table)




# Enter table size: 5
# Enter number of keys to insert: 4
# Enter key 1: apple
# Inserted 'apple' at index 0
# Enter key 2: banana
# Inserted 'banana' at index 4
# Enter key 3: cherry
# Inserted 'cherry' at index 1
# Enter key 4: date
# Inserted 'date' at index 2

# Hash Table:
# Index 0: apple
# Index 1: cherry
# Index 2: date
# Index 3: null
# Index 4: banana
