# dtype -  Its used to check the data type of elements of the array. It returns the data type of the array elements.


import numpy as np

array = np.array([1, 2, 3, 4, 5])
print("Data type of array elements:", array.dtype) #output: int64 - as it contains only integer values


#example 2
array2 = np.array([1, 2.5, 3]) #output: float64 - as it contains a float value (chahe sirf ek hi kyu na ho)

print("Data type of array elements:", array2.dtype)