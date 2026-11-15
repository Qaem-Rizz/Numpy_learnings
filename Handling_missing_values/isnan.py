"""to handle missing values, numpy gives us certain functions.


firstly, 'np.isnan(array_name)' is used to return TRUE/FALSE for whether a NOT A NUMBER value is present in an array or not - just to check"""


import numpy as np

arr = np.array([1,2,3,np.nan , 4, np.nan , 5])

print(np.isnan(arr))


#we can also use second approach:


#used np.any() becaause np.isnan returns an array of boolean values and not a single value:

if np.any(np.isnan(arr)) :
    print ("Non numeric values")