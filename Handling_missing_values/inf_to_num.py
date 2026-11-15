"""
for converting inf to num values, the syntax is same as it was in NAN_TO_NUM, the difference is the value section... there we have to pass POSINF, NEGINF in place of nan"""



import numpy as np

arr = ([1,2,-np.inf,3,4,10,np.inf,5,6])

cleaned_arr = np.nan_to_num(arr , posinf = 1000 , neginf = -1000)
print(cleaned_arr)