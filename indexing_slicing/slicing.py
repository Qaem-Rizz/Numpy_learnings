# SLICING : it is a way to access a range of elements in an array. It allows you to extract a portion of the array based on specified start and end indices.

#syntax: array[start:end:step] where:
# start: The index of the first element to include in the slice (inclusive).    
# end: The index of the first element to exclude from the slice (exclusive).
# step: The step size or stride between elements in the slice. It determines how many elements
"""
default value of start is 0, end is the length of the array, and step is 1.
If start is omitted, it defaults to 0. If end is omitted, it defaults to the length of the array. If step is omitted, it defaults to 1."""


import numpy as np

array = np.array([10, 20, 30, 40, 50])

print("Original array:", array)

print ("Slicing from index 1 to 4:", array[1:4])  # Output: [20 30 40] only returns elements from index 1 to 3 (4 is excluded)

print ("Slicing from index 0 to 3:", array[0:3])  # Output: [10 20 30] only returns elements from index 0 to 2 (3 is excluded)

print ("Slicing from index 2 to the end:", array[2:])  # Output: [30 40 50] returns elements from index 2 to the end of the array -  as STOP index is not given, it will take the length of the array as the end index.

print ("Slicing from the start to index 3:", array[:3])  # Output: [10 20 30] returns elements from the start of the array to index 2 (3 is excluded) - as start index is not given, it will take 0 as the start index.

print ("Slicing with a step of 2:", array[::2])  # Output: [10 30 50] returns every second element from the array - as start and end indices are not given, it will take the default values of 0 and length of the array respectively.

"""we can also pass a negative step value to slice the array in reverse order. In this case, the start index should be greater than the end index."""

print ("Slicing with a negative step:", array[::-1])  # Output: [50 40 30 20 10] returns the array in reverse order.