#complexidade de algoritmos

class Numero:
    def __init__(self, n=0):
        self.__numero = n
        self.__ganhou = []
    def getNumero(self):
        return self.__numero
    def setNumero(self, n):
        self.__numero = n
    def getGanhou(self):
        return self.__ganhou
    def setGanhou(self,g):
        self.__ganhou = g
    def maiorQue(self, n):
        return self.getNumero()>n.getNumero()
    def ganhouDe(self, n):
        self.__ganhou.append(n.getNumero())
    def maiores(self):
        return self.getNumero(), max(self.getGanhou())    

    
