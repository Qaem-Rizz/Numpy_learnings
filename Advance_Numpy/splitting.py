"""Numpy gives you 4 types of splitting functions.

np.split() - for equal split sizes.. if the asked split value can't be processed, a Value Error arises... so we can say numpy.split() is used to divide an array into equal-sized subarrays. The number of splits must perfectly divide the size of the array along the chosen axis. If equal division is not possible, NumPy will raise an error.


np.array_split() - works like split(), but it allows uneven splitting. This is useful when the array size does not divide evenly by the number of splits. NumPy will distribute the extra elements automatically.


np.vsplit() -  performs vertical splitting, meaning it divides a matrix row-wise (along axis=0). It works only on arrays with 2 or more dimensions. 


np.hsplit() - performs horizontal splitting, which divides the array column-wise (axis=1). This is helpful when separating feature columns in datasets."""


import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10])

print(np.split(array, 2))  #here, 2 IS THE SPLIT SIZE..


array2 = np.array([1,2,3,4,5])


print(np.array_split(array2, 2)) #the first array among the divided arrays will contain the extra element


array3 = np.array([[1,2,3,13],
           [4,5,6,14],
           [7,8,9,15],
           [10,11,12,16]
           ])


print(np.vsplit(array3, 2)) #rowwise divide krdega

print(np.hsplit(array3,2)) #column k hisab se divide krega..