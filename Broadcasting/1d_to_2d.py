import numpy as np

array1d = np.array ([1,2,3]) #VECTOR


array2d = ([[1,2,3], #MATRIX
            [4,5,6],
            [7,8,9]
            ])

"""
note that here the addition will be done automatically by numpy CORRESPONDINGLY as per rows """

result = array1d + array2d #matrix + vector

print(result)




#example 2: lets try and see what happens when we try to braodcast arrays with diff dimensions:

array3 = np.array([[1,2,3],
                   [4,5,6]
                   ])

array4 = np.array([10,20])

#new_result = array3 + array4


#print(new_result) ValueError: operands could not be broadcast together with shapes (2,3) (2,) 


#what we gotta do here is use the .RESHAPE function of Numpy to reshape either of the arrays:

array_new = array3.reshape(6)

new_result = array_new + array4 # ValueError: operands could not be broadcast together with shapes (6,) (2,)

print(new_result)

"""even now, the elements numbers should be same to perform braodcasting.."""