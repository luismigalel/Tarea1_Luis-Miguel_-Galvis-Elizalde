#!/usr/bin/env python
# coding: utf-8

# 4) La probabilidad de que cuando se lanza una moneda n veces resulte
# un número k de veces cara (sello) está dada por la expresión $\left(\frac{n}{k}\right)/2^{n}$
# Usando el módulo que ya escribió escriba una rutina dentro de Tarea1
# que calcule e imprima (a) la probabilidad de que si se hace este exper-
# imento 100 veces, el resultado sean 10 veces cara, (b) la probabilidad
# de que caiga cara más de 30 veces.

# In[1]:


from funciones import *


# a) n = Número de lanzamientos. k = Número de veces.

# In[9]:


b=Binomial(100, 10)/(2**100)
print("La probabilidad es: ", b)


# In[5]:


Binomial(100, 10)


# b)

# In[10]:


c=Binomial(100, 30)/(2**100)
print("La probabilidad es: ", c)


# 2.1) 
# 
# Checks

# Veamos que sucede cuando introducimos números de tipo flotante.

# In[12]:


Factorial(1.5)


# In[13]:


Binomial(2.3, 2)


# Veamos la forma de nuestro triangulo de Pascal.

# In[14]:


Pascal(4)

