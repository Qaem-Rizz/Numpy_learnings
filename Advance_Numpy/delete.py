# np.delete is used to delete the element from a certain index in an array in numpy.

# syntax is :   np.delete(array_name, index, axis = None) axis is None for flattened array- Note that it returns a new array and doesn't changes the original array.


import numpy as np

array = np.array([1,2,3,4,5])

new_array = np.delete(array , 3, axis = None)

print(new_array) #[1,2,3,5] will get printed



#NOW FOR 2D ARRAY:

# axis = 0 means deletion along rows
# axis = 1 means deletion along columns


array2d = np.array ([[1,2,3],
                     [4,5,6]])

array_new = np.delete(array2d , 0 , axis = 0) # it will delete the whole first row , i.e , the row with index 0 in a 2D array

print(array_new)