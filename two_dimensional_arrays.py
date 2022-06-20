# In 2-D Array, data are represented in two dimensions.
# Data are stored two dimensions as rows and columns.
# Matrix is example of 2 D Array.

# Array.

two_d_array = [[1,2,3], [4,5,6], [7,8,9]]

# Accessing rows of a 2 D array.

first_row = two_d_array[0]

print("First row of the 2-D array", first_row)

# Accessing value of a column in that particular row.

column_value_of_a_row = first_row[2]

print("Value of a column of a particular row,", column_value_of_a_row)

# Creating a 2 D Array.

desired_number_of_rows = int(input("How many rows do you want your Array to have?"))
created_array = []

for row in range(desired_number_of_rows):
    created_array.append([int(row) for row in input(f"Enter the {row + 1} row elements").split()])
print("Before updaing the array", created_array)

# Updating a 2 D Array.

# Change the value of second rows third column.
created_array[1][2] = [4, 5]

#Change the value of third row's second column.
created_array[2][1] = 101

print("Updated ARRAY:", created_array)

# Traversing over a 2 D Array.

for rows in created_array:

    for columns in rows:

        print(columns, end=' ')
    print()

# Length of array.

print("Length of the given array is", len(created_array))

# Slicing and indexing over the arrays.


second_and_third_rows = created_array[1:3]

print("The second and third rows of the given array are", second_and_third_rows)

third_element_of_the_second_row = created_array[1][2]

print("Third element of the second row of the Array is", third_element_of_the_second_row)

# Deleting elements from Array.

print("Array before deleting", created_array)

del(created_array[1])

print("After deleting the second row in the array", created_array)
