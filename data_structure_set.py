# Set does not allow duplicate values.
# Sets don't support indexing.
# Sets are mutable.


# Defining Sets.

# set() takes object an argument. And the object should be an iterable.

first_set = set((56, 100, 0, 10,67, 95))

second_set = {65,89,12,34,10,78,1,5,24}

# The below for loop will not print the elements of the set in order they are placed.
# Sets are unordered.

for item in second_set:
    print(item)

# Adding elements to set.

second_set.add(101)
first_set.add(102)

# Removing items from sets.

second_set.discard(101)
first_set.discard(102)

# Union of sets.

union_of_sets = second_set | first_set

print("Union of sets", union_of_sets)

# Intersection of sets.

intersection_of_sets = first_set & second_set

print("Intersection of sets", intersection_of_sets)

# Comparasions between sets.
# The output would be a boolean. 
# It will be True only if the sets are either super set or sub set of each other.

comparsion_of_sets = second_set == first_set

print("Comparasion between sets", comparsion_of_sets)

print(second_set)
print(first_set)