"""Broadcasting applies specific rules to find whether two arrays can be aligned for operations or not that are:

Check Dimensions: 

Ensure the arrays have the same number of dimensions or expandable dimensions.

eg: [1,2,3] + [4,5,6] = [5,7,9]


Dimension Padding: 

If arrays have different numbers of dimensions the smaller array is left-padded with ones.

Shape Compatibility: 

Two dimensions are compatible if they are equal or one of them is 1.
If these conditions aren't met NumPy will raise a ValueError

eg: [1,2,3] + [4,5] = error


Expanding single element:

if one of the arrays has lets say only one element, Numpy expands it to make the dimensions same with other array

eg: array_new = arr * 2"""


import numpy as np

array = np.array([1,2,3,4,5])

new_arr = array * 5

print(new_arr)