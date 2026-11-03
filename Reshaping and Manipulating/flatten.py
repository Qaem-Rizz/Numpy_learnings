"""Flattening an Array can be simply taken as converting a multi-dimensional array into a single-dimensional array. In this article, we will discuss how to flatten an array in Python using different methods.

2 methods are there to do it:

(1) using flatten() method of numpy module - this returns a copy , so the original array remains unchanged.

(2) using ravel() method of numpy module - this returns a flattened array, but it is a view of the original array, so any changes made to the flattened array will affect the original array.
"""


import numpy as np

array_2d = np.array([[1, 2], 
                     [3, 4], 
                     [5, 6]])


print(array_2d.flatten())  # Output: [1 2 3 4 5 6]

print (array_2d.ravel())  # Output: [1 2 3 4 5 6]
"""output same hi hai, bs returned array copy hai ya original change hui hai wo difference hai."""

