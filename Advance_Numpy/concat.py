# numpy provides an inBuilt function to concatenate two existing arrays along an Axis.

#syntax:   np.concatenate( (array1, array2)  , axis )

# note that AXIS = 0 -> VERTICAL STACKING : arrays ek dusre ke neeche judti hain
#           AXIS = 1 -> HORIZONTAL STACKING : arrays ek dusre ke sath judti hain


import numpy as np

array1 = np.array ([1,2,3])

array2= np.array ([4,5,6])


array_whole = np.concatenate((array1,array2) , axis =0)

print(array_whole) #output : [1,2,3,4,5,6] as its 1D array, EK HI AXIS HOTA HAI FOR 1D ARRAY - AXIS =0



# 2D array examples:
# For axis=0, arrays must have the same number of columns.
# For axis=1, arrays must have the same number of rows.

array3 = np.array([[1, 2, 3],
                   [4, 5, 6]])


array4 = np.array([[7, 8, 9],
                   [10, 11, 12]])

array_vertical = np.concatenate((array3, array4), axis=0)
print("axis=0 (vertical):")
print(array_vertical)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

array_horizontal = np.concatenate((array3, array4), axis=1)
print("axis=1 (horizontal):")
print(array_horizontal)
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]