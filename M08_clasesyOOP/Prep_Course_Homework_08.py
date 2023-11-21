#!/usr/bin/env python
# coding: utf-8

# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor

# In[1]:

class Vehiculo():
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = cilindrada
        self.cilindrada = cilindrada

# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>

# In[5]:


class Vehiculo():
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = cilindrada
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0

    def Acelerar(self, velocidad):
        self.velocidad += velocidad
        print("La velocidad es de: ", self.velocidad)

    def Frenar(self, velocidad):
        if velocidad > self.velocidad:
            print("Error de frenos")
        self.velocidad -= velocidad
        print("La velocidad es de: ", self.velocidad)

    def Doblar(self, grados):
        self.direccion += grados
        print("La direccion es de: ", self.direccion)


# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

# In[6]:

vehiculo1 = Vehiculo("Azul", "Moto", 3)
vehiculo2 = Vehiculo("Rojo", "Auto", 2)
vehiculo3 = Vehiculo("Verde", "Avion", 4)

vehiculo1.Acelerar(120)
vehiculo2.Acelerar(175)
vehiculo3.Acelerar(150)

vehiculo1.Frenar(90)
vehiculo2.Frenar(45)
vehiculo3.Frenar(100)

vehiculo1.Doblar(90)
vehiculo2.Doblar(75)
vehiculo3.Doblar(180)

# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. 
# Y otro método que muestre color, tipo y cilindrada

# In[12]:


class Vehiculo():
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0

    def Acelerar(self, velocidad):
        self.velocidad += velocidad
        print("La velocidad es de: ", self.velocidad)

    def Frenar(self, velocidad):
        if velocidad > self.velocidad:
            print("Error de frenos")
        self.velocidad -= velocidad
        print("La velocidad es de: ", self.velocidad)

    def Doblar(self, grados):
        self.direccion += grados
        print("La direccion es de: ", self.direccion)

    def Estado(self):
        print("Se encuentra a una velocidad de: ", self.velocidad, "Con una direccion de: ", self.direccion)

    def DatosVehiculo(self):
        print("Color> ", self.color, "Tipo> ", self.tipo, "Cilindrada>", self.cilindrada)



# In[13]:



vehiculo4 = Vehiculo("Azul", "Moto", 3)

vehiculo4.Acelerar(120)

vehiculo4.Frenar(90)

vehiculo4.Doblar(90)

vehiculo4.Estado()

vehiculo4.DatosVehiculo()


# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 7<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

# In[33]:


class FuncionesM7():

    def __init__(self) -> None:
        pass

    def is_primo(self, numero):
        if numero < 2:
            return False
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True

    
    def more_repeat(self, lista):
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

    
    def convert(self, valor, medida, destino):
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

    def factorial(self, num):
        if (num < 0):
            return print('No se puede calcular el factorial de un número negativo')
        elif (type(num) != int):
            return print('No se puede calcular el factorial de un número no entero')
        elif (num == 1):
            return num
        else:
            num = num * self.factorial(num - 1)
        return num


# 6) Probar las funciones incorporadas en la clase del punto 5

# In[28]:

funciones = FuncionesM7()

print(funciones.is_primo(3))
print(funciones.factorial(5))
print(funciones.convert(1, 'K', 'C'))


# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# In[55]:

list_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(funciones.more_repeat(list_numbers))


# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

# In[1]:


import funcionesm7


funciones_module = funcionesm7.FuncionesM7()


print(funciones_module.is_primo(3))
print(funciones_module.factorial(5))
print(funciones_module.convert(1, 'K', 'C'))
list_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(funciones_module.more_repeat(list_numbers))



mi_variable = "Python"
def mi_funcion():
    pass
print(dir())