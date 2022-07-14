#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request
import pandas
import json


# In[2]:


request1=urllib.request.urlopen("https://petstore.swagger.io/v2/pet/findByStatus?status=available")

lines1 = request1.read()
data = json.loads(lines1)


# In[3]:


df = pandas.DataFrame.from_records(data)


# In[4]:


print(df.head)


# In[5]:


print(df.shape[0])

