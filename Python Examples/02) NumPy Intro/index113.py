import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])




# Access 3-D Arrays
# To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.


# Access the third element of the second array of the first array:





# Example Explained
# arr[0, 1, 2] prints the value 6.

# And this is why:

# The first number represents the first dimension, which contains two arrays:
# [[1, 2, 3], [4, 5, 6]]
# and:
# [[7, 8, 9], [10, 11, 12]]
# Since we selected 0, we are left with the first array:
# [[1, 2, 3], [4, 5, 6]]

# The second number represents the second dimension, which also contains two arrays:
# [1, 2, 3]
# and:
# [4, 5, 6]
# Since we selected 1, we are left with the second array:
# [4, 5, 6]

# The third number represents the third dimension, which contains three values:
# 4
# 5
# 6
# Since we selected 2, we end up with the third value:
# 6

