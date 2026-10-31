# In numpy arrays, SHAPE refers to the dimensions of the array, while SIZE refers to the total number of elements in the array.


import numpy as np

# Create a 2D numpy array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Get the shape of the array
shape_2d = array_2d.shape #output: (2, 3)  # This means the array has 2 rows and 3 columns

# Get the size of the array
size_2d = array_2d.size  #output : 6  # This means the array has a total of 6 elements

print("Shape of 2D array:", shape_2d)
print("Size of 2D array:", size_2d)