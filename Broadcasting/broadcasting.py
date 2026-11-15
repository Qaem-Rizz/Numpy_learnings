"""
now lets try to again solve the previous question (price list) while using the numpy fucntions"""

import numpy as np

price = np.array ([100,200,300])

discount = 10

new_price  = price  - (price * (discount /100))

print (new_price)


"""
as we can see, no ooping needed here.... this is the basic idea, we can perform operations directly in numpy arrays"""