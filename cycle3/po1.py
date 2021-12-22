import matplotlib.pyplot as plt
import numpy as np


x = np.array([2001, 2002, 2003, 2004, 2005, 2006, 2007])
y = np.array([24000, 22500, 19700, 17500, 14500, 10000, 5800])
plt.plot(x,y, linestyle = 'dashed',color='red',marker='*',ms=20,mec='green')

plt.show()

