import numpy as np

M = np.array([[2,3,4], [3,45,8], [4,8,78]])
print('\n\nMatrix M\n', M)
# Transposing the Matrix M
print('\n\nTranspose as M.T\n', M.T)

if M.T.all() == M.all():
    print("Matrix is symmetric")
else:
    print("The given matrix is not symmetric")

arr=np.array([[1,3], [3,-5]])   
    
if (arr.transpose() == -arr).all():
  print("matrix is skew symmetric")