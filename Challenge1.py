#!/usr/bin/env python
# coding: utf-8

# In[15]:


n = input('Enter a number\n')
try:
    n=int(n)
    m=0
    x=0
    y=1

    while m!=n-2:
        z=x+y
        x=y
        y=z
        m=m+1

    print(z)      
except: 
     print('Enter a number Next time')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




