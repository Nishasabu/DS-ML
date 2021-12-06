import numpy as np
array1=np.array([[1,2],[5,6]])
array2 =np.array([[10,11],[1,2]])
# add 2 matrix
a=np.matrix(array1)
b=np.matrix(array2)
c=a+b;
print(c)
#substract two matrix
c=a-b;
print(c)
#multiply individual elements
c=a*b;
print(c)
#Divide the elements of the matrices
c=a/b;
print(c)
#Perform matrix multiplication
c=a.dot(b)
print(c)
  # Display transpose of the matrix
M1 = np.array([[3, 6, 9], [5, -10, 15], [4,8,12]])
M2 = M1.transpose()
print(M2)
 # Sum of diagonal elements of a matrix
M1 = np.array([[3, 6, 9], [5, -10, 15], [4,8,12]])
print(np.trace(M1))