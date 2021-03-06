#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
student = pd.read_csv('student_scores.csv')
student.head()


# In[7]:


student.describe()


# In[8]:


student.info()


# In[10]:


import matplotlib.pyplot as plt
Xax=student.iloc[:,0]
Yax=student.iloc[:,1]
plt.scatter(Xax,Yax)
plt.xlabel("No.of hours")
plt.ylabel("Score")
plt.title("Student scores")
plt.show()


# In[11]:


#Perform the simple linear regression model
#Equation: Y=w0+w1.x
#Here Y(marks)=w0+w1.x
#Create x as hours and Y as marks
X = student.iloc[:, :-1]
y = student.iloc[:, 1]
print(X)


# In[12]:


print(y)


# In[13]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train)


# In[14]:


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


# In[15]:


print(regressor.intercept_)


# In[16]:


print(regressor.coef_)


# In[20]:


y_pred = regressor.predict(X_test)
for(i,j) in zip(y_test,y_pred):
 if i!=j:
  print("Actual value:",i,"Predicted value:",j)
print("Number of mislabeled points from test data set :", (y_test != y_pred).sum())


# In[21]:


from sklearn import metrics
print("Mean Absolute error :", metrics.mean_absolute_error(y_test,y_pred))
print("Mean Squared error :", metrics.mean_squared_error(y_test,y_pred))
print("Root Mean Squared error :", np.sqrt(metrics.mean_squared_error(y_test,y_pred)))


# In[23]:


import matplotlib.pyplot as plt
c=X_test['Hours'].count()
xax=np.arange(c)
print(xax)
X_axis = np.arange(len(xax))
plt.bar(X_axis-0.2, y_test, 0.6, label='Actual')
plt.bar(X_axis+0.2, y_pred, 0.6, label='Predicted')
plt.xlabel("Test Records")
plt.ylabel("Marks")
plt.title("Student Score prediction")
plt.legend()
plt.show()


# In[24]:


#multiple linear regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
advertising = pd.read_csv('Company_data.csv')
advertising.head()


# In[25]:


advertising.describe()


# In[27]:


advertising.info()


# In[28]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.pairplot(advertising, x_vars=['TV', 'Radio', 'Newspaper'],
            y_vars='Sales', height=5, aspect=1, kind='scatter')
plt.show()


# In[29]:


#perform the multiple linear regression model
#Equation : Y=w0+w1.x1 + w2.x2 + w3.x3
#Here Y(sales)=w0+w1.x1(TV)+w2.x2(Radio)+w3.x3(Newspaper)
#create x and Y as sales
X = advertising.iloc[:, :-1]
print(X)


# In[30]:


y = advertising.iloc[:, -1]
print(y)


# In[31]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
print(X_train)


# In[32]:


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


# In[33]:


print(regressor.intercept_)


# In[34]:


print(regressor.coef_)


# In[35]:



y_pred = regressor.predict(X_test)
for(i,j) in zip(y_test,y_pred):
    if i!=j:
        print("Actual value :",i,"Predicted value :",j)
print("Number of mislabeled points from test data set :", (y_test != y_pred).sum())


# In[36]:


from sklearn import metrics
print("Mean Absolute error :", metrics.mean_absolute_error(y_test,y_pred))
print("Mean Squared error :", metrics.mean_squared_error(y_test,y_pred))
print("Root Mean Squared error :", np.sqrt(metrics.mean_squared_error(y_test,y_pred)))


# In[37]:


import matplotlib.pyplot as plt
c=X_test['TV'].count()
xax=np.arange(c)
print(xax)
X_axis = np.arange(len(xax))
plt.bar(X_axis-0.2, y_test, 0.6, label='Actual')
plt.bar(X_axis+0.2, y_pred, 0.6, label='Predicted')

plt.xlabel("Sales")
plt.ylabel("Actual/Predicted")
plt.title("Sales prediction")
plt.legend()
plt.show()


# In[ ]:




