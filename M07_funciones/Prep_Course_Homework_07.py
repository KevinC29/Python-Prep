#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:

def lista_primos(lista):
    lista_primos = []
    for i in lista:
        if es_primo(int(i)):
            lista_primos.append(i)
    return lista_primos

lis_completa = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lis_primos = lista_primos(lis_completa)
print(lis_primos)



# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:

def mas_repetido(lista):
    list_repeat = []
    list_count = []
    for i in lista:
        if i in list_repeat:
            index = list_repeat.index(i)
            list_count[index] += 1
        else:
            list_repeat.append(i)
            list_count.append(1)
    
    max_count = list_count.index(max(list_count))
    max_repeat = list_repeat[max_count]

    return max_repeat, max(list_count)

list_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(list_numbers)
print(mas_repetido(list_numbers))

# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:

def convert(valor, medida, destino):
    if medida == 'C':
        if destino == 'F':
            return (valor * 9/5) + 32
        elif destino == 'K':
            return valor + 273.15
        else:
            return print('No se puede convertir a la misma medida')
    elif medida == 'F':
        if destino == 'C':
            return (valor - 32) * 5/9
        elif destino == 'K':
            return (valor - 32) * 5/9 + 273.15
        else:
            return print('No se puede convertir a la misma medida')
    elif medida == 'K':
        if destino == 'C':
            return valor - 273.15
        elif destino == 'F':
            return (valor - 273.15) * 9/5 + 32
        else:
            return print('No se puede convertir a la misma medida')
    else:
        return print('No se puede convertir')

print('1 grado Celsius a Celsius:', convert(1, 'C', 'C'))
print('1 grado Celsius a Kelvin:', convert(1, 'C', 'K'))
print('1 grado Celsius a Farenheit:', convert(1, 'C', 'F'))
print('1 grado Kelvin a Celsius:', convert(1, 'K', 'C'))
print('1 grado Kelvin a Kelvin:', convert(1, 'K', 'K'))
print('1 grado Kelvin a Farenheit:', convert(1, 'K', 'F'))
print('1 grado Farenheit a Celsius:', convert(1, 'F', 'C'))
print('1 grado Farenheit a Kelvin:', convert(1, 'F', 'K'))
print('1 grado Farenheit a Farenheit:', convert(1, 'F', 'F'))


# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:


grades = ['K', 'C', 'F']
for i in grades:
    for j in grades:
        print('1 grado', i, 'a', j, ':', convert(1, i, j))


# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:


def factorial(num):
    if (num < 0):
        return print('No se puede calcular el factorial de un número negativo')
    elif (type(num) != int):
        return print('No se puede calcular el factorial de un número no entero')
    elif (num == 1):
        return num
    else:
        num = num * factorial(num - 1)
    return num

print(factorial(5))


lambda_producto = lambda x, y: x * y
lambda_producto(3, 4)

print(lambda_producto(3, 4))