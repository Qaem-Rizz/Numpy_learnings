# For Arrays, numpy has a np.array function which converts python lists into numpy arrays. This is useful for performing mathematical operations on the data.

#syntax: np.array([ele 1, ele 2, ele 3, ...])
import numpy as np
cookies = np.array([10, 20, 30, 40, 50])  #beech se commas gayab hojaenge

print(cookies)



#array with default values : prints array with initialized values of 0. This is useful when you want to create an array of a specific shape but don't have any data to fill it with yet.
#syntax: np.zeros(shape) .... where shape : (x)for 1D  array, (x,y) for 2D array, (x,y,z) for 3D array
zeros_array = np.zeros((3, 4))  # 3 rows and 4 columns
print(zeros_array)