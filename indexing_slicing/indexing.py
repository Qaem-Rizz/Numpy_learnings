#INDEXING: it refers to the process of accessing individual elements or subsets of data structures, such as lists, tuples, strings, or arrays, using their respective indices. In Python, indexing starts at 0 for the first element, and negative indices can be used to access elements from the end of the structure.


import numpy as np

array = np.array([10, 20, 30, 40, 50])

print(array[0])  # Accessing the first element (10)

print(array[2])  # Accessing the third element (30)

print(array[-1])  # Accessing the last element (50)

print(array[10]) # This will raise an IndexError since the index is out of bounds