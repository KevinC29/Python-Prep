#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:


list_city = ['Quito', 'Cuenca', 'Obelisco', 'Madrid', 'Barcelona']
print(list_city)

# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

print(list_city[1])


# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:


print(list_city[1:4])


# 4) Visualizar el tipo de dato de la lista

# In[12]:


print(type(list_city))


# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:


print(list_city[2:])


# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:


print(list_city[:4])
    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:


list_city.append('Cuenca')
list_city.append('Londres')
#No da error por que se puede agregar elementos repetidos
print(list_city)


# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:


list_city.insert(3, 'Loja')
print(list_city)

# In[21]:

list_city.insert(3, 'Esmeraldas')
print(list_city)


# 9) Concatenar otra lista a la ya creada

# In[22]:


list_city2 = ['Guayaquil', 'Machala', 'Milan']
list_city = list_city + list_city2
print(list_city)


list_city.extend(['Paris','Roma','Guayaquil'])
print(list_city)


# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:

print(list_city.index('Cuenca'))
#La unica particularidad es que se toma el primer elemento que encuentra


# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:

# print(list_city.index('Cuenca2'))
print("Da error ya que no encuentra el elemento")


# 12) Eliminar un elemento de la lista

# In[25]:


list_city.remove('Madrid')
print(list_city)


# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:


# list_city.remove('Madrid2')
print("Da error ya que no encuentra el elemento")

# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:

value = list_city.pop()
print(value)


# 15) Mostrar la lista multiplicada por 4

# In[29]:

print(list_city * 4)


# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:

tuple_numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(tuple_numbers)


# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:


print(tuple_numbers[10:16])

# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:


print(20 in tuple_numbers)
print(30 in tuple_numbers)

# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:


exist = 'París'
if exist in list_city:
    exit = True
    print("El elemento existe", exist)
else:
    list_city.append('Paris')
    print("El elemento no existe: ", exist)


# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:


cont_list = list_city.count('Cuenca')
cont_tuple = tuple_numbers.count(1)

print("Cantidad de veces que se encuentra el elemento en la lista: ", cont_list)
print("Cantidad de veces que se encuentra el elemento en la tupla: ", cont_tuple)

# 21) Convertir la tupla en una lista

# In[52]:


tuple_list = list(tuple_numbers)
print(tuple_list)

# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:


var_1, var_2, var_3 = tuple_numbers[:3]
print(var_1, var_2, var_3)


# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:


dic_city = {'ciudad': list_city, 'pais': 'Ecuador', 'continente': 'America'}
print(dic_city)


# 24) Imprimir las claves del diccionario

# In[59]:


print(dic_city.keys())

# 25) Imprimir las ciudades a través de su clave

# In[61]:


print(dic_city['ciudad'])

