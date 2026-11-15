"""
another function to handle infinite values in Numpy:


syntax: NP.ISINT(ARRAY_NAME) - will return an array of boolean (T/F) values..
"""

import numpy as np

arr = np.array([1,2,3,4,5,np.inf , 6,7 , -np.inf])

cleaned_arr = np.isinf(arr)
print(cleaned_arr)