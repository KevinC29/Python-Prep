class FuncionesM7():

    def __init__(self) -> None:
        pass

    def is_primo(self, lista):
        list_primos = []

        for i in lista:
            if not isinstance(i, int):
                raise ValueError("La lista contiene valores no numericos")
            if i < 2:
                list_primos.append(False)
            for j in range(2, i):
                if i % j == 0:
                    list_primos.append(False)
            list_primos.append(True)
        return list_primos
    
    def more_repeat(self, lista):
        list_repeat = []
        list_count = []
        for i in lista:
            if not isinstance(i, int): #En este caso validamos que la lista contenga solo valores numericos
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

    def factorial(self, num):
        if (num < 0):
            raise ValueError('No se puede calcular el factorial de un número negativo')
        elif (type(num) != int):
            raise ValueError('No se puede calcular el factorial de un número no entero')
        elif (num == 1):
            return num
        else:
            num = num * self.factorial(num - 1)
        return num
