import matplotlib.pyplot as plt
import numpy as np

x = np.array(["walking", "cycling", "car", "bus","train"])
y = np.array([29,15,35,18,3])

plt.bar(x,y, color="#4CAF50",width=0.1)
plt.xlabel("-mode of Transport")
plt.ylabel("frequency")
plt.show()
