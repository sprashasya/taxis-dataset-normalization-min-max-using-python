#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns


# In[4]:


df=sns.load_dataset("taxis")


# In[5]:


df.head()


# In[6]:


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()


# In[7]:


scaler.fit(df[["distance","fare","tip"]])


# In[9]:


scaler.transform(df[["distance","fare","tip"]])


# In[ ]:




