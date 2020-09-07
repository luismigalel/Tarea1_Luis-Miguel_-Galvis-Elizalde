#!/usr/bin/env python
# coding: utf-8

# In[32]:


import matplotlib.pyplot as plot
import numpy as np


#  1)
# A continuacion crearemos una función que nos permita calcular el factorial.

# In[3]:


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


# 2) Ahora vamos a crear la función para los coeficientes binomiales.

# In[4]:


def Binomial(n, k):
    return (Factorial(n))/((Factorial(k))*(Factorial(n-k)))


# 3) Definimos la función que nos entregara el triangulo de Pascal en un archivo .txt

# En primera instancia se debe ampliar el número de iteraciones para funciones que tiene mi pc pues tiene problemas con ello.

# In[9]:


import sys
print(sys.getrecursionlimit())


sys.setrecursionlimit(5000)


# In[33]:


def Pascal(n):
    pascal=open("Pascal-%i.txt"%n,"w") #El nombre del archivo esta supeditado al n.
    i=0
    a=1
    for t in range(n):
        if t+1==10**a:
            pascal.write("n=%i"%(t+1))
            pascal.write(" "*(n-i+5-a))
            a+=1
            i+=1
        else:
            pascal.write("n=%i"%(t+1))
            pascal.write(" "*(n-1+5))
        for j in range(t+1):
            pascal.write(str(Binomial(t,j)))
            pascal.write(" ")
                
        i=+1
        pascal.write("\n")   #Pasamos a la liguiente fila.
    
    pascal.close


# In[ ]:





# In[ ]:




