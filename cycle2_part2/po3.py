import numpy as np;



x = np.arange(1,31).reshape(5,6)



print("x-> big matrix :\n",x)



y=x[1:4,2:5]



z = np.arange(2,11).reshape(3,3)



y = np.multiply(y,z)



x[1:4,2:5] = y

print("final replaced matrix:\n ",x)




