import numpy as np
array1=np.array([[1,2,3,4],[3,4,5,6],[7,8,9,1],[4,5,6,7]])
print("Matrix:",array1)
#display elements of 1st an 2nd column
print("display 1st and 2nd column in 2nd and 3rd row")
x=array1[1:3,:2]
print(x)
print("display 2nd and 3rd element of first row")
y=array1[:1,1:3]
print(y)

