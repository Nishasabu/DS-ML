import numpy as np
M1 = np.array([[3, 6], [4, 2]])
M2 = np.array([[9, 2], [1, 2]])
M3=np.array([[2,4],[3,1]])
Mul = M1.dot(M2) 
mul1=M3.dot(Mul)
print("Matrix1:\n",M1)
print("Matrix2:\n",M2)
print("Matrix3:\n",M3)
print("multiplication of 3 matrices") 
print(mul1)