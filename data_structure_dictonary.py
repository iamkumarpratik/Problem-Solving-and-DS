# Dictonaries are key-value pair based.
# Dictonaries are mutable.
# Every value has a key in the dictonary.
# You cannot store a value without a key in a dictonary.

# Creating dictonary.

first_dictonary = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}

second_dictonary = dict([(0, "Zero"), (1, "One")])

# Accessing elements of a dictonary.
# Here we pass a key to get the value of that key in the dictonary.
print(first_dictonary[2])

# Adding and modifying data in a dictonary.

first_dictonary[1] = 'Ten'

second_dictonary[10] = 'Ten'

# Deleting values from a dictonary.

first_dictonary.pop(3)

# How to see all the keys, values, and items of a dictonary.

keys = first_dictonary.keys()
values = first_dictonary.values()
items = first_dictonary.items()
print("Keys", keys)
print("Values", values)
print("Items", items)


print(first_dictonary)
print(second_dictonary)

# Emptying dictonary.

first_dictonary.clear()
