#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("customer_data.csv")
dataset.head()


# In[6]:


x=dataset.iloc[:,[3,4]].values
print(x)


# In[82]:


kmeansmodel = KMeans(n_clusters=5)
y_Kmeans = kmeansmodel.fit_predict(x)
plt.scatter(x[y_Kmeans == 0,0],x[y_Kmeans ==0,1],s=80,c='blue',label='customer 1')
plt.scatter(x[y_Kmeans == 1,0],x[y_Kmeans ==1,1],s=80,c='orange',label='customer 2')
plt.scatter(x[y_Kmeans == 2,0],x[y_Kmeans ==2,1],s=80,c='green',label='customer 3')
plt.scatter(x[y_Kmeans == 3,0],x[y_Kmeans ==3,1],s=80,c='yellow',label='customer 4')
plt.scatter(x[y_Kmeans == 4,0],x[y_Kmeans ==4,1],s=80,c='pink',label='customer 5')
plt.show()


# In[94]:


kmeansmodel = KMeans(n_clusters=5)
y_Kmeans = kmeansmodel.fit_predict(x)
plt.scatter(x[y_Kmeans == 0,0],x[y_Kmeans ==0,1],s=80,c='blue',label='customer 1')
plt.scatter(x[y_Kmeans == 1,0],x[y_Kmeans ==1,1],s=80,c='orange',label='customer 2')
plt.scatter(x[y_Kmeans == 2,0],x[y_Kmeans ==2,1],s=80,c='green',label='customer 3')
plt.scatter(x[y_Kmeans == 3,0],x[y_Kmeans ==3,1],s=80,c='yellow',label='customer 4')
plt.scatter(x[y_Kmeans == 4,0],x[y_Kmeans ==4,1],s=80,c='pink',label='customer 5')
centers= kmeansmodel.cluster_centers_
plt.scatter(centers[:,0],centers[:,1], s=120, c= 'red',label='centroid')
plt.title("customer data")
plt.xlabel("Annual income(K$)")
plt.ylabel("spending score(1-100)")
plt.legend()
plt.show()


# In[ ]:




