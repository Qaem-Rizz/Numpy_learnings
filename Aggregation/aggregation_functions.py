# Aggregate functions in Numpy are used to perform operations on an entire array, returning a single value. These functions are optimized for performance and can handle large datasets efficiently. Some common aggregate functions include:

# - np.sum(): Computes the sum of all elements in the array.
# - np.mean(): Computes the mean (average) of all elements in the array.
# - np.std(): Computes the standard deviation of all elements in the array.
# - np.var(): Computes the variance of all elements in the array.
# - np.min(): Returns the minimum value in the array.
# - np.max(): Returns the maximum value in the array.
# - np.prod(): Computes the product of all elements in the array.
# - np.cumsum(): Computes the cumulative sum of the elements in the array: CUMULATIVE SUM - it is the sum of the current element and all previous elements in the array.
# - np.cumprod(): Computes the cumulative product of the elements in the array: CUMULATIVE PRODUCT - it is the product of the current element and all previous elements in the array.



import numpy as np

array = np.array([1, 2, 3, 4, 5])

print("sum is : " ,np.sum(array)) #output: 15
print("mean is : " ,np.mean(array)) #output: 3.0
print("standard deviation is : " ,np.std(array)) #output: 1.4142135623730951
print("variance is : " ,np.var(array)) #output: 2.0
print("minimum value is : " ,np.min(array)) #output: 1
print("maximum value is : " ,np.max(array)) #output: 5
print("product is : " ,np.prod(array)) #output: 120
print("cumulative sum is : " ,np.cumsum(array)) #output: [ 1  3  6 10 15]
print("cumulative product is : " ,np.cumprod(array)) #output: [ 1  2  6 24 120]