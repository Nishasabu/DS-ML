#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split

from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree


# In[2]:


with open("tickets.txt") as f:
    tickets = f.read().strip().split("\n")

with open("labels_4.txt") as f:
    labels = f.read().strip().split("\n")


# In[8]:


X_train, X_test, y_train, y_test = train_test_split(tickets, labels, test_size=0.1, random_state=1337)


# In[9]:


vectorizer = CountVectorizer()
svm = LinearSVC()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)
_ = svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)

print(classification_report(y_test, y_pred))


# In[10]:


print(confusion_matrix(y_test, y_pred))


# In[ ]:




