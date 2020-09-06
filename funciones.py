#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plot
import numpy as np


# ## 1)
# A continuacion crearemos una funcion que nos permita calcular el factorial

# In[5]:


def Factorial(x):
    if x<0:
        return "error"  
    elif x==0:
        return 1 #Por definición el factorial de cero es 1.
    else:
        producto=1
        for i in range(1, x+1):
            producto=producto*i
    return producto


# casa
# 

# In[6]:


print("Me agarró la madrugada aprendiendo")


# In[7]:


a=2
b=3.14


# In[8]:


np.round(a+b, decimals=2)


# In[9]:


np.sqrt(np.pi)


# In[10]:


22222


# In[11]:


333


# In[ ]:




