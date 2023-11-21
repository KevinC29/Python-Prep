#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:


list_empty = []
for i in range(-15,0):
    list_empty.append(i)

print(list_empty)

# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:

# Si, es posible
i = 0
while i < len(list_empty):
    if list_empty[i] % 2 == 0:
        print("Numero par con ciclo while: ", list_empty[i])
    i += 1

# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:


for i in list_empty:
    if i % 2 == 0:
        print("Numero par con ciclo for: ", i)


# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:

for i in list_empty[:3]:
    print("Primeros 3 elementos: ", i)

# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:


enum = enumerate(list_empty)
print(list(enum))

for i, e in enumerate(list_empty):
    print("Indice: ", i, "Elemento: ", e)

# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:


lista = [1,2,5,7,8,10,13,14,15,17,20]


# In[11]:


for i in range(1,21):
    if i not in lista:
        lista.insert(i-1,i)

print(lista)


# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:


list_fibonacci = []
for i in range(30):
    if i == 0:
        list_fibonacci.append(0)
    elif i == 1:
        list_fibonacci.append(1)
    else:
        list_fibonacci.append(list_fibonacci[i-1] + list_fibonacci[i-2])

print(list_fibonacci)

# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:

list_fibonacci_sum = sum(list_fibonacci)
print(list_fibonacci_sum)


# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:

#Ultimos 5 valores de la serie fibonacci
print(list_fibonacci[-6:])
new_list_f = list_fibonacci[-6:]
for i in range (1, len(new_list_f)):
    print(new_list_f[i]/new_list_f[i-1])

# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

pos =  enumerate(cadena)

for i, e in pos:
    if e == 'n':
        print(i)


# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:


new_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
for i in new_dict:
    print(i)


# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:


list_cadena = list(cadena)
for i in list_cadena:
    print(i)


# In[45]:


recorre = iter(cadena)
largo = len(cadena)
for i in range(0, largo):
    print(next(recorre))


# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:


list_a = [1,2,3,4,5]
list_b = ['a','b','c','d','e']

tuple_a = tuple(zip(list_a, list_b))
tuple_b = list(zip(list_a, list_b))
print(tuple_a)
print(tuple_b)


# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:

lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
new_list = []

for i in range(len(lis)):
    if lis[i] % 7 == 0:
        new_list.append(lis[i])

print(new_list)

new_list_2 = [i for i in lis if i % 7 == 0]
print(new_list_2)

# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:

lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
count = 0



# In[51]:


for i in lis:
    if type(i) == list:
        count += len(i)
    else:
        count += 1


# In[57]:


print("La cantidad de elementos es: ", count)


# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:

lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

for i in range(len(lis)):
    if type(lis[i]) != list:
        lis[i] = [lis[i]]

print(lis)

for i, e in enumerate(lis):
    if type(e) != list:
        lis[i] = [e]
print(lis)

