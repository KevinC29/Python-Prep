#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

var = 5

if var > 0:
    print("Respuesta punto 1: Es mayor a cero")
elif var == 0:
    print("Respuesta punto 1: Es igual a cero")
else:
    print("Respuesta punto 1: Es menor a cero")


# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:


booleano = True
num_a = 5
num_b = 10

if(type(booleano) == type(num_a)):
    print("Respuesta punto 2: Son del mismo tipo de dato")
else:
    print("Respuesta punto 2: No son del mismo tipo de dato")

if(type(num_a) == type(num_b)):
    print("Respuesta punto 2: Son del mismo tipo de dato")
else:
    print("Respuesta punto 2: No son del mismo tipo de dato")

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

val_num = 1
while val_num <= 20:
    if val_num % 2 == 0:
        print("Respuesta punto 3: El número " + str(val_num) + " es par")
    else:
        print("Respuesta punto 3: El número " + str(val_num) + " es impar")
    val_num += 1


# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:


for i in range(0, 6):
    print("Respuesta punto 4: " + str(i) + " elevado a la potencia 3 es igual a: " + str(i**3))


# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:


var_for = 5
for i in range(0, var_for):
    print("Respuesta punto 5: Ciclo número: " + str(i))


# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

num_f = 5
result_fd = 1

if type(num_f) == int and num_f > 0:
    print("Respuesta punto 6: Factoreo de " + str(num_f) + " es: ")
    while num_f > 1:
        result_fd = result_fd * num_f
        num_f -= 1
    print(str(result_fd))
else:
    print("Respuesta punto 6: La variable no contiene un número entero mayor a 0")


# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

num_w=0
while(num_w<3):
    print("Respuesta punto 7: Ciclo while número: " + str(num_w))
    for i in range(0, 2):
        print("Respuesta punto 7: Ciclo for número: " + str(i))
    num_w+=1


# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:


for i in range(0, 2):
    print("Respuesta punto 8: Ciclo for número: " + str(i))
    num_w=0
    while(num_w<2):
        print("Respuesta punto 8: Ciclo while número: " + str(num_w))
        num_w+=1


# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

cont_div = 0
for i in range(0, 31):
    if i < 2:
        print("Respuesta punto 9: " + str(i) + " no es un número primo")
        continue
    cont_div = 0
    for j in range(2, i):
        if i % j == 0:
            cont_div += 1
    if(cont_div > 0):
        print("Respuesta punto 9: " + str(i) + " no es un número primo")
    else:
        print("Respuesta punto 9: " + str(i) + " es un número primo")

# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:


for i in range(0, 31):
    if i < 2:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print("Respuesta punto 10: " + str(i) + " es un número primo")


# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:

cant_repite_1 = 0
cont_div = 0
for i in range(0, 31):
    if i < 2:
        print("Respuesta punto 11: " + str(i) + " no es un número primo")
        continue
    cont_div = 0
    for j in range(2, i):
        cant_repite_1 += 1
        if i % j == 0:
            cont_div += 1
    if(cont_div > 0):
        print("Respuesta punto 11: " + str(i) + " no es un número primo")
    else:
        print("Respuesta punto 11: " + str(i) + " es un número primo")


cant_repite_2 = 0
for i in range(0, 31):
    if i < 2:
        continue
    for j in range(2, i):
        cant_repite_2 += 1
        if i % j == 0:
            break
    else:
        print("Respuesta punto 11: " + str(i) + " es un número primo")

# In[57]:

print("Cantidad de veces que se repite el ciclo for del punto 9: " + str(cant_repite_1))

print("Cantidad de veces que se repite el ciclo for del punto 10: " + str(cant_repite_2))


# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

num_start = 99
while(num_start <= 300):
    num_start += 1
    if num_start % 12 != 0:
        continue
    print("Respuesta punto 12: " + str(num_start) + " es divisible por 12")
    


# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:

num_p = 1
while True:

    if num_p <= 2:
        print("Respuesta punto 13: " + str(num_p) + " no es un número primo")
        num_p += 1
        continue
    
    for i in range(2, num_p):
        if num_p % i == 0:
            print("Respuesta punto 13: " + str(num_p) + " no es un número primo")
            break
    else:
        print("Respuesta punto 13: " + str(num_p) + " es un número primo")

    num_input = input("Ingrese 1 si quiere conocer el siguiente numero primo: ")

    if num_input.isdigit():
        num_input = int(num_input)
        if num_input == 1:
            num_p += 1
        else:
            break
    else:
        print("Respuesta punto 13: El número ingresado no es válido")


# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:

num_div_mul = 100
while(num_div_mul <= 300):
    if (num_div_mul%6==0):
        print("Respuesta punto 14: El primer numero divisible para 3 y multiplo de 6 es: ", num_div_mul)
        break
    else:
        num_div_mul += 1
