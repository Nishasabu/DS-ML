import numpy as np 
# create square matrix
matrix = np.random.randint(1,10,size=(2,2))
print(matrix)
#inverse
print(np.linalg.inv(matrix))
#rank
rank = np.linalg.matrix_rank(matrix)
print(rank)
det = np.linalg.det(matrix)
print(int(det))

