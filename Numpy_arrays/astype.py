#ASTYPE is used for type conversion in numpy arrays. It allows you to convert the data type of an array to a specified type. For example, you can convert an array of integers to floats or vice versa. The syntax for using astype is as follows:

#SYNTAX: array.astype(new_data_type)

import numpy as np
array = np.array([1, 2, 3, 4, 5]) #integer array

array_float = array.astype(float) #convert to float
print("Original array:", array) #output: [1 2 3 4 5]
print("Converted array:", array_float) #output: [1. 2. 3. 4. 5.]




#example2:

float_array = np.array([1.5, 2.5, 3.5]) #float array
array_int = float_array.astype(int) #convert to integer

print("Converted array:", array_int)
print(array_int.dtype) #output: int64 - as it contains only integer values