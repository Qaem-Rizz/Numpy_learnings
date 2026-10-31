# Ndim stands for Number of dimensions. This script is used to calculate the number of dimensions in a given dataset.


import numpy as np

array_1d = np.array([1, 2, 3, 4, 5]) #output: 1 - as its a 1D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]]) #output: 2 - as its a 2D array with 2 rows and 3 columns
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) #output: 3 - as its a 3D array

print("Number of dimensions in array_1d:", array_1d.ndim)
print("Number of dimensions in array_2d:", array_2d.ndim)
print("Number of dimensions in array_3d:", array_3d.ndim)