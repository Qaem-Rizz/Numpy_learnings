"""
the nan_to_num() function changes the non numeric values to a certain value , the default is zero."""


import numpy as np

arr = np.array([1,2,3,4,np.nan , 5,6,np.nan])


cleaned_arr = np.nan_to_num(arr) #default 0 



print(cleaned_arr)


cleaned_arr2 = np.nan_to_num(arr , nan = 5) #changed to 5
print(cleaned_arr2)