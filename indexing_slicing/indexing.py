#INDEXING: it refers to the process of accessing individual elements or subsets of data structures, such as lists, tuples, strings, or arrays, using their respective indices. In Python, indexing starts at 0 for the first element, and negative indices can be used to access elements from the end of the structure.


import numpy as np

array = np.array([10, 20, 30, 40, 50])

print(array[0])  # Accessing the first element (10)

print(array[2])  # Accessing the third element (30)

print(array[-1])  # Accessing the last element (50)

print(array[10]) # This will raise an IndexError since the index is out of bounds



#note : the above code is for 1D array indexing. For multi-dimensional arrays, you can use multiple indices to access elements. example:

array2 = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

print(array2[0, 1])  # Accessing the element in the first row and second column (2)