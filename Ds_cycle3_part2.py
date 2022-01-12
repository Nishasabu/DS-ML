#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
col=['sepal_length','sepal_width','petal_length','petal_width','type']
iris=pd.read_csv("iris.csv",names=col)
print("shape:",iris.shape)
print("*********")
print("First five rows")
print(iris.head())
print("*********")
print("Last five rows")
print(iris.tail())
print("*********")
print("Size:",iris.size)
print("*********")
print("no of samples available for each variety")
print(iris["type"].value_counts())
print("*********")
print(iris.describe())


# In[3]:


sns.set_style("whitegrid")
iris = sns.load_dataset("iris")
sns.pairplot(iris, kind="kde")
sns.pairplot(iris, kind="scatter",hue="species",markers=["o", "s", "D"])
sns.pairplot(iris, kind="hist")
sns.pairplot(iris, kind="reg",hue="species",markers=["o", "s", "D"])


# In[4]:


sns.displot(
data=iris,
x="sepal_length", y="sepal_width"
)
sns.relplot(
data=iris,
x="petal_length", y="petal_width"
)
sns.histplot(
data=iris,
x="petal_length", y="petal_width"
)


# In[ ]:




