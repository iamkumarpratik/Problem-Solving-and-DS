# The list is a Python data structure. 
# It can store elements of multiple types of data. 
# You can use indexing with lists. 
# Lists allow you to store duplicate data.
# Lists are mutable, i.e. they are modifiable.

first_list = [98, 98, 98, 98]

# Append takes an object and adds it to the list.
first_list.append(1)

# Insert takes two objects, first, the index at which you want to insert the element, and second the object.
first_list.insert(1, 2)

# Extend takes iterable an argument.

first_list.extend(range(3, 9))

# Pop removes the last element of the list.

first_list.pop() 

# Remove takes the element value as an argument and removes it from the list.

first_list.remove(3)

# Sort function sorts the list into ascending order by default.

first_list.sort(reverse=True)

# The count function takes the element value as an argument and tells the count of its repetition in the list. 
num = 98
count = first_list.count(num)
print(f"Count of {num} in the list is {count}.")

# The index takes the object/element value as an argument and returns the index. 
# If the number is repeated in the list, it will return the index of the first occurrence of the element.

idx_val = 98

idx = first_list.index(idx_val)

print(f"The index of {idx_val} is {idx}")

print(first_list)

# Clear clears the whole list.

first_list.clear()

print("Cleared list", first_list)
