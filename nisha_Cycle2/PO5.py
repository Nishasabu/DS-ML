import numpy as np
a = np.arange(0, 30, 2)
print(a)
a1= a[2:9:2]
print(a1)
s = slice(2, 9 , 2) 
print(a[s])
print(a[-3:30])
a2=a[0:30:3]
print(a2)