#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

num = 1
print("Respuesta punto 1: ", num)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

const = 8.5
print("Respuesta punto 2: ", type(const))



# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

print("Respuesta punto 3: ", type(num))



# 4) Crear una variable que contenga tu nombre

# In[2]:


name = 'kevin'
print("Respuesta punto 4: ", name)

# 5) Crear una variable que contenga un número complejo

# In[3]:


num_complex = 1 + 2j
print("Respuesta punto 5: ", num_complex)


# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

print("Respuesta punto 6: ", type(num_complex))



# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416
print("Respuesta punto 7v0: ", round(pi, 4))
round_pi = round(pi, 4)
print("Respuesta punto 7v1: ", round_pi)


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

boolean_1 = 'True'
boolean_2 = True
#No son lo mismo uno es un string y el otro es un boleano
print("Respuesta punto 8: No son lo mismo")


# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print("Respuesta punto 9: ", "Valor 1: ", type(boolean_1), "Valor 2: ", type(boolean_2))


# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

num_int = 1
num_float = 1.5
print("Respuesta punto 10v0: ", num_int + num_float)
sum_int_float_v1 = num_int + num_float
print("Respuesta punto 10v1: ", sum_int_float_v1)
sum_int_float_v2 = 1 + 1.5
print("Respuesta punto 10v2: ", sum_int_float_v2)


# 11) Realizar una operación de suma de números complejos

# In[2]:

sum_complex = (1 + 2j) + (3 + 4j)
print("Respuesta punto 11v0: ", sum_complex)
sum_complex_a = 3 + 4j
sum_complex_b = 1 + 2j
print("Respuesta punto 11v1: ", sum_complex_a + sum_complex_b)
sum_complex_c = sum_complex_a + sum_complex_b
print("Respuesta punto 11v2: ", sum_complex_c)


# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:


sum_real_complex = (1 + 2j) + 3.1416
print("Respuesta punto 12v0: ", sum_real_complex)
sum_real_complex_a = 4 + 4j
sum_real_complex_b = 5
print("Respuesta punto 12v1: ", sum_real_complex_a + sum_real_complex_b)


# 13) Realizar una operación de multiplicación

# In[5]:

print("Respuesta punto 13v0: ", 5*4)
num_a = 6
num_b = 8
print("Respuesta punto 13v1: ", num_a*num_b)
mult = num_a*num_b
print("Respuesta punto 13v2: ", mult)



# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:


print("Respuesta punto 14v0: ", 2**8)
pot = 2**8
print("Respuesta punto 14v1: ", pot)
num_pot_a = 2
pot_num_a = 8
print("Respuesta punto 14v2: ", num_pot_a**pot_num_a)
result = num_pot_a**pot_num_a
print("Respuesta punto 14v3: ", result)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

print("Respuesta punto 15v0: ", 27/4)
quotient = 27/4
print("Respuesta punto 15v1: ", quotient)
dividend = 27
divisor = 4
print("Respuesta punto 15v2: ", dividend/divisor)
result_div = dividend/divisor
print("Respuesta punto 15v3: ", result_div)


# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

print("Respuesta punto 16v0: ", int(quotient))
quotient_int = int(quotient)
print("Respuesta punto 16v1: ", quotient_int)
quotient_int_div = 27//4
print("Respuesta punto 16v2: ", quotient_int_div)


# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:


residue = 27 % 4
print("Respuesta punto 17v0: ", residue)
rest_dividend = 27
rest_divisor = 4
print("Respuesta punto 17v1: ", rest_dividend % rest_divisor)
result_rest = rest_dividend % rest_divisor
print("Respuesta punto 17v2: ", result_rest)


# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

print("Respuesta punto 18v0: ", 4*quotient_int + residue)
operand = 4
get_result = operand * quotient_int + residue
print("Respuesta punto 18v1: ", get_result)


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

print("Respuesta punto 19v0: ", 'hola1' + 'mundo2')
var_alfa_a = 'hola1'
var_alfa_b = 'mundo1'
result_alfa = var_alfa_a + var_alfa_b
print("Respuesta punto 19v1: ", result_alfa)


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:


print("Respuesta punto 20v0: ", "2" == 2)
num_bool = "2"
num_int = 2
print("Respuesta punto 20v1: ", num_bool == num_int)
print("Respuesta punto 20v2: No son iguales por que son de diferente tipo de dato")


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

print("Respuesta punto 21v0: ", int("2") == 2)
num_bool_int = int("2")
num_int_compare = 2
result_num_compare = num_bool_int == num_int_compare
print("Respuesta punto 21v1: ", result_num_compare)
num_bool_compare = "2"
num_int_bool = str(2)
print("Respuesta punto 21v2: ", num_bool_compare == num_int_bool)


# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

result_change = float('3.8')
print("Respuesta punto 22v0: ", "Por que no es del tipo de dato float por la coma")
print("Respuesta punto 22v1: ", "Para que la conversión sea exitorsa debe ser 3.8")


# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:


value = 3
value -= 1
print("Respuesta punto 23v0: ", value)
value_a = 3
value_a = value_a - 1
print("Respuesta punto 23v1: ", value_a)


# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:


operation = 1 << 2
print("Respuesta punto 24v0: ", operation)
print("Respuesta punto 24v1: ", "Por que se desplaza 2 posiciones a la izquierda o lo equivalente a 0100 en binario")
print("Respuesta punto 24v2: ", "El sistema de numeración binario es un sistema de numeración en el que los números se representan utilizando solamente las cifras cero y uno, es decir, base dos.")


# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:


# operation_sum = 2 + '2' #No esta permitido por que son de diferente tipo de dato
# print("Respuesta punto 25v0: ", operation_sum)
print("Respuesta punto 25v1: ", "No esta permitido por que son de diferente tipo de dato")
operation_sum_a = 2 + 2
print("Respuesta punto 25v2: ", operation_sum_a)
operation_sum_b = '2' + '2'
print("Respuesta punto 25v3: ", operation_sum_b)
print("Respuesta punto 25v4: ", "Si los dos operandos fueran del mismo tipo de dato va cambiar el resultado ya que uno seria de tipo entero y el otro de tipo cadena")



# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

value_int_a = 2
value_str_b = '2Hola Mundo'

operation_int_str = value_a * value_str_b
print("Respuesta punto 26v0: ", operation_int_str)


#Conversiondes de tipos de datos

#Conversion de str a bool
bool_str_a = 'True'
boolean_a = bool(bool_str_a)
print("Respuesta punto 27v1: ", boolean_a)


#Conversion de numeros binarios a decimal

num_bin = 1010

num_dec = int(str(num_bin), 2)
print("Respuesta punto 27v2: ", num_dec)

print("Respuesta punto 27v3: ", (1*(2**3) + 0*(2**2) + 1*(2**1) + 0*(2**0)))