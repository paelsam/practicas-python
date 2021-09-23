#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


# Componentes principales de Pandas
# La Serie es una Columna 
# El DataFrame es una tabla multidimensional con muchas series


# In[5]:


# Vamos a crear una serie: 
ventas = pd.Series([12,20,15], index = ["Ene", "Feb", "Mar"])
ventas


# In[10]:


# Podemos extraer el valor de las series como si fuera una lista
# Con solo saber la posicion en la que se encuentra
ventas[0]


# In[9]:


# Y si tiene su etiqueta es mucho mejor 
ventas["Feb"]


# In[11]:


# Las etiquetas que forman el índice no necesitan ser diferentes. Pueden ser de cualquier tipo (numérico,
# textos, tuplas...) siempre que sea posible aplicar la función hash sobre ellas.

# Es de destacar que el lazo entre una etiqueta y un valor se mantendrá salvo que lo modifiquemos
# explícitamente. Esto quiere decir que filtrar una serie o eliminar un elemento de la serie, por ejemplo, no
# va a modificar las etiquetas asignadas a cada valor.

# Otro comentario importante es al respecto de la inmutabilidad del índice de etiquetas: aun cuando es
# posible asignar a una serie un nuevo conjunto de etiquetas a través del atributo index, intentar modificar
# un único valor del index va a devolver un error.


# In[13]:


# Los valores de una serie son inmutables
# Para ver el tipo de Series que tenemos utilizamos la funcion "dtype"
ventas.dtype


# In[15]:


# Podemos acceder a los objetos que contienen los índices y los valores a través de los
# atributos index y values de la serie, respectivamente.
ventas.index


# In[16]:


ventas.values


# In[17]:


# La serie tiene, además, un atributo name, atributo que también encontramos en el índice. Una vez los
# hemos fijado, se muestran junto con la estructura al imprimir la serie.
ventas.name = "Ventas 2021"


# In[18]:


ventas


# In[19]:


# Mira como tambien podemos poner el atributo name a los indices
ventas.index.name = "Meses"


# In[20]:


ventas


# In[21]:


# El atributo axes nos da acceso a una lista con los ejes de la serie (solo contiene un elemento al
# tratarse de una estructura unidimensional
ventas.axes


# In[22]:


# El atributo shape es como la funcion len.
# Nos manda el numero de elementos de la Serie
ventas.shape


# In[ ]:




