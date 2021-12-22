import matplotlib.pyplot as plt
import numpy as np

x = np.array(["mon", "tue", "wed", "thu","fri"])
y = np.array([300,450,150,400,650])
plt.subplot(1, 2, 1)
plt.plot(x,y)

plt.plot(x,y, linestyle = 'dotted',color='cyan',marker='H',mec='black',mfc='magenta')

plt.xlabel("days of week")
plt.ylabel(" sales drinks")

#plot2

x = np.array(["mon", "tue", "wed", "thu","fri"])
y = np.array([400, 500, 350, 300, 500])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.plot(x,y, linestyle = 'dashed',color='yellow',marker='D',mec='red',mfc='green')
plt.xlabel("days of week")
plt.ylabel(" sales food")
plt.show()
