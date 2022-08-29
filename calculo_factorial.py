from clasePilaEncadenada import Pila

class calculo:
    __pila = None
    
    def __init__(self):
        self.__pila = Pila()
    
    def calcular_factorial(self, numero):
        assert isinstance(numero,int)
        res = numero
        numero -= 1
        if numero >= 0:
            self.__pila.insertar(res)
            self.calcular_factorial(numero)
    
    def mostrar(self):
        res = 1
        if not self.__pila.vacia():
            while self.__pila.getCantidad() > 0:
                val = self.__pila.suprimir()
                res = res*val
                print('{}'.format(val))
        print('Resultado: {}'.format(res))
                


            
            
        