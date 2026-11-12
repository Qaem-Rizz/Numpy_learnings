#APPEND is used to add elements to teh end of an existing array. Similar to the insert function, it also creates a new array and the original array remains unchanged.
#  the syntax is : np.append(name of array, [element])  - pass the list of elements if its more than one.



import numpy as np

array = np.array([10,20,30])

print(array)


new_array = np.append(array, [40,50]) # 40 and 50 will get added to the end of array 

print(new_array)