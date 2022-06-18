# Tuple is a collection Python objects separated by commas.
# Tuples are immuatable.
# Tuples are similar to list, but they cannot be modified.

first_tuple = (1,2,3, "your name")

print("Type", type(first_tuple))

# Iterating over elements in tuple.

for item in first_tuple:
    print(item)


# Adding elements to a tuple.

first_tuple = first_tuple + (4,5,6,6)

# Indexing with tuple.

print(first_tuple[3])

# Tuples are immutable.

# first_tuple[2] = 1 

# Above line when uncommented should generate type error.

# Slicing with tuple.

print(first_tuple[1:4])

# Count with tuple.

print(first_tuple.count(6))

print(first_tuple)

# Deleting a tuple.
del first_tuple

# If the below lines is uncommented, it should generate Name error.
# print(first_tuple)

