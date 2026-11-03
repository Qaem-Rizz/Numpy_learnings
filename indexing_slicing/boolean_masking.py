"""Also called FILTERING.

syntax: array[boolean_mask] -  in place of boolean mask , write your condition, the whole array is traversed and only the elements satisfying the given condition are returned."""


import numpy as np

array = np.array([10, 20, 30, 40, 50])

print(array[array > 30])  # returns elements greater than 30 - gives result as [40 50] - a List form.

print(array[array < 30])  # returns elements less than 30 - gives result as [10 20] - a List form.

print(array[array == 30])  # returns elements equal to 30 - gives result as [30] - a List form.

print(array[array != 30])  # returns elements not equal to 30 - gives result as [10 20 40 50] - a List form.

#etc etc etc...


"""BOOLEAN MASKING is way more faster to traverse over data in a large dataset - so extensively used in data science and machine learning applications."""

