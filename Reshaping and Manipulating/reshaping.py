"""Reshaping means , changing the dimensions of an array without changing its data. It is a very useful operation in data analysis and machine learning, as it allows us to manipulate the shape of our data to fit the requirements of different algorithms and models.

the thing is - the number of elements remains the same in the reshaped array as in the original array. So, if we have an array with 12 elements, we can reshape it into a 3x4 array or a 4x3 array, but we cannot reshape it into a 2x5 array, as that would require 10 elements.
in this example, we will see how to reshape a 1D array into a 2D array using the reshape() method in NumPy."""

import  numpy as np

array = np.array([1 , 2 , 3, 4, 5, 6])

reshaped_array = array.reshape(2, 3)  # reshaping the 1D array into a 2D array with 2 rows and 3 columns - noe that original array has 6 elements, and our reshaped array will have same number of elements which is 2 x3 =6.

"""also note that, the reshaping operation does not change the original array, it creates a new array with the specified shape. So, if we print the original array after reshaping, we will still see the same 1D array with 6 elements.
"""

print("Original array:", array)
print("Reshaped array:\n", reshaped_array)


#example 2: reshaping a 2D array into 1D array

array2 = np.array([[1, 2, 3], 
                   [4, 5, 6]])

reshaped_array2 = array2.reshape(6)  # reshaping the 2D array into a 1D array with 6 elements - note that original array has 6 elements, and our reshaped array will have same number of elements which is 6.
print("Original array 2:\n", array2)
print("Reshaped array 2:\n", reshaped_array2)