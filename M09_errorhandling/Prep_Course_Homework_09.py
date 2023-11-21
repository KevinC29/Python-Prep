#!/usr/bin/env python
# coding: utf-8

# ## Manejo de errores

# 1) Con la clase creada en el módulo 8, tener en cuenta diferentes casos en que el código pudiera arrojar error. Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero ¿qué pasa si se envía otro tipo de dato?

# In[1]:

import funcionesm8


def more_repeat(self, lista):
    list_repeat = []
    list_count = []
    for i in lista:
        if not isinstance(entrada_usuario, int): #En este caso validamos que la lista contenga solo valores numericos
            raise ValueError("La lista contiene valores no validos") #Caso contrario muestra un error 

        if i in list_repeat:
            index = list_repeat.index(i)
            list_count[index] += 1
        else:
            list_repeat.append(i)
            list_count.append(1)
        
    max_count = list_count.index(max(list_count))
    max_repeat = list_repeat[max_count]

    return max_repeat, max(list_count)

# 2) En la función que hace la conversión de grados, validar que los parámetros enviados sean los esperados, de no serlo, informar cuáles son los valores esperados.

# In[5]:


def convert(self, valor, medida, destino):
    if not isinstance(valor, int) or not isinstance(medida, str) or not isinstance(destino, str): #Validamos que los datos sean correctos
        raise ValueError("Alguno de los valores no es correcto") #Caso contrario muestra un error 

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


# 3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2<br>
# Creacion del objeto incorrecta<br>
# Creacion correcta del objeto<br>
# Metodo valor_modal()<br>
# 
# Se puede usar "raise ValueError()" en la creación de la clase para verificar el error. Investigar sobre esta funcionalidad.

# In[9]:

import unittest
from funcionesm8 import FuncionesM7


class PruebaDeCristalTest(unittest.TestCase):

    def test_objeto_incorrecto(self):
        objeto = FuncionesM7(1)
        self.assertIsInstance(objeto, FuncionesM7)

    def test_objeto_correcto(self):
        objeto = FuncionesM7()
        self.assertIsInstance(objeto, FuncionesM7)

    def test_list_correcto(self):
        objeto = FuncionesM7()
        list_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        num1, num2 = objeto.more_repeat(list_numbers)
        self.assertEqual(num1, 1)
        self.assertEqual(num2,16)

    def test_list_incorrecto(self):
        num1 = 0
        num2 = 0
        objeto = FuncionesM7()
        list_numbers = ["a",2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        num1, num2 = objeto.more_repeat(list_numbers)
        self.assertEqual(num1, 0)
        self.assertEqual(num2, 0)


# 4) Probar una creación incorrecta y visualizar la salida del "raise"

# In[13]:

unittest.main(argv=[""], verbosity=2, exit=False)

# 6) Agregar casos de pruebas para el método verifica_primos() realizando el cambio en la clase, para que devuelva una lista de True o False en función de que el elemento en la posisicón sea o no primo

# In[14]:

class PruebaDeCristalTest(unittest.TestCase):

    def test_list_primos_correcto(self):
        objeto = FuncionesM7()
        list_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        list_primos = objeto.is_primo(list_numbers)
        self.assertIsInstance(list_primos, list)

    def test_list_primos_incorrecto(self):
        objeto = FuncionesM7()
        list_numbers = [1,"a",3,4,5,6,7,8,9,10,11,12,13,14,15,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        list_primos = objeto.is_primo(list_numbers)
        self.assertIsInstance(list_primos, list)


unittest.main(argv=[""], verbosity=2, exit=False)

# 7) Agregar casos de pruebas para el método conversion_grados()

# In[17]:

class PruebaDeCristalTest(unittest.TestCase):

    def test_conversion_correcto(self):
        result = 0
        objeto = FuncionesM7()
        result = objeto.convert(1, 'K', 'C')
        self.assertEqual(result, -272.15)
        self.assertIsInstance(result, float)

    def test_conversion_incorrecto(self):
        result = 0
        objeto = FuncionesM7()
        result = objeto.convert("a", 'K', 'C')
        self.assertEqual(result, 0)


unittest.main(argv=[""], verbosity=2, exit=False)


# 8) Agregar casos de pruebas para el método factorial()

# In[20]:


class PruebaDeCristalTest(unittest.TestCase):

    def test_factorial_correcto(self):
        result = 0
        objeto = FuncionesM7()
        result = objeto.factorial(5)
        self.assertEqual(result, 120)
        self.assertIsInstance(result, int)

    def test_factorial_incorrecto(self):
        result1 = 0
        result2 = 0
        objeto = FuncionesM7()
        result1 = objeto.factorial(-1)
        result2 = objeto.factorial("a")
        self.assertEqual(result1, 0)
        self.assertEqual(result2, 0)


unittest.main(argv=[""], verbosity=2, exit=False)