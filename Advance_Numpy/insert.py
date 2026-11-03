"""
Inserting in Numpy arrays is different from inserting in Python lists. In Numpy, you can use the `numpy.insert()` function to insert values into an array at specified indices. This function allows you to specify the axis along which to insert the values, making it versatile for multi-dimensional arrays.
But the thing is - this function creates a new array with the inserted values, rather than modifying the original array in place. This is an important distinction to keep in mind when working with Numpy arrays, as it can affect performance and memory usage, especially with large datasets."""

#Syntax: numpy.insert(array, index, value to be inserted, axis=None)
# The AXIS parameter is optional. If not specified, the input array is flattened before insertion.
# For 2D array - axis 0 means inserting along rows, and axis 1 means inserting along columns.


import numpy as np

array = np.array([1, 2, 3, 4, 5])

np.insert(array, 2, 99, axis=None) # ye sirf ek new array bani hai pr store nahi hui kahi, we have to store it to print it and re-use it.

result_array = np.insert(array, 2, 99, axis=None) # Now we are storing the new array in result_array

print (result_array) # Output: [ 1  2 99  3  4  5]

"""Now , inserting in 2D array - axis 0 means inserting along rows, and axis 1 means inserting along columns."""

array_2d = np.array([[1, 2, 3], 
                     [4, 5, 6]])

#inserting a new row at index 1
new_array2d = np.insert(array_2d, 1, [99, 99, 99], axis=0) # Inserting a new row at index 1 - so the value added is a 2d array row, and the Axis=0 shows that we are inserting along rows.
print("inserting along row, new 2d array:\n", new_array2d)

#inserting a new column at index 1
new_array2d_col = np.insert(array_2d, 1, [99, 99], axis=1) # Inserting a new column at index 1 - so the value added is a 2d array column, and the Axis=1 shows that we are inserting along columns.
print("inserting along column , new 2d array:\n", new_array2d_col)