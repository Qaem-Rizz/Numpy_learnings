# For the default value to be One 
#syntax: np.ones(shape)

import numpy as np

ones_array = np.ones((3, 4))  # 3 rows and 4 columns
print(ones_array)




#Default value, but the value is decided by the user.
#syntax: np.full(shape, fill_value) - in the place of fill_value, you can put any value you want to fill the array with.

full_array = np.full((3, 4), 7)  # 3 rows and 4 columns, filled with the value 7
print(full_array)