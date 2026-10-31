#identity matrix: it is a square matrix in which all the elements of the principal diagonal are ones and all other elements are zeros. It is denoted by I_n, where n is the size of the matrix. The identity matrix serves as the multiplicative identity in matrix multiplication, meaning that any matrix multiplied by the identity matrix will result in the original matrix.

#syntax: np.eye(shape)
import numpy as np

identity_matrix = np.eye(3)  # 3x3 identity matrix : 
# [1 ,0 ,0]
# [0 ,1 ,0]
# [0 ,0 ,1]

print(identity_matrix)