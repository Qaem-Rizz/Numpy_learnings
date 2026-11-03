"""FANCY INDEXING : it is a way to access elements in an array using an array of indices. It allows you to select specific elements from the array based on their positions.

always Note , that in fancy indexing - pass the indexes of array in a List form"""


import numpy as np

array = np.array([10, 20, 30, 40, 50])

print("Original Array:", array)

print ("Fancy Indexing Example: " , array[[0, 2, 4]])
# Fancy indexing using a list of indices
# will return the elements at positions 0, 2, and 4 from the original array - gives result as [10 30 50]  - a List form.

