"""
STACKING means combining two existing arrays together. for this, 2 functions are there:

vstack - row wise ek ke upar ek
hstack - column wise horizontal line me

"""

import numpy as np


arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])


print(np.vstack((arr1,arr2)))

print(np.hstack((arr1,arr2)))