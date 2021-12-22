import matplotlib.pyplot as plt
import numpy as np
x = np.array(['jan','feb','mar','april','may','jun','july','aug','sep','oct','nov','dec'])
y1 = np.array([173,153,195,147,120,144,148,109,174,130,172,131])
y2 = np.array([189,189,105,112,173,109,151,197,174,195,177,161])
y3 = np.array([185,185,126,134,196,183,112,133,200,145,167,116])
font1={'size':18}
plt.scatter(x,y1,color='pink')
plt.scatter(x,y2,color='yellow')
plt.scatter(x,y3,color='blue')
plt.xlabel("Month of year",fontdict=font1)
plt.ylabel("Sales of segments")
plt.show()
