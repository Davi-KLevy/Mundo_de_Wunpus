import copy
from pysat.formula import CNF
from pysat.solvers import Solver
class Jogador:

    def __init__(self):
        self.direcao = 1
        self.x = 0
        self.y = 0

    def vira_direita(self):
        self.direcao += 1

    def vira_esquerda(self):
        self.direcao -= 1

    def andar_frente(self):
        if self.direcao % 4 == 1:
            self.y += 1
        elif self.direcao % 4 == 2:
            self.x += 1
        elif self.direcao % 4 == 3:
            self.y -= 1
        elif self.direcao % 4 == 0:
            self.x -= 1
        print("[ {} / {} ]".format(self.x, self.y))
        return [self.x, self.y]

    def retorna_frente(self):
        if self.direcao % 4 == 1:
            return [self.x, self.y + 1]
        elif self.direcao % 4 == 2:
            return [self.x + 1, self.y]
        elif self.direcao % 4 == 3:
            return [self.x, self.y - 1]
        elif self.direcao % 4 == 0:
            return [self.x - 1, self.y]


class BancoDeDados:

    def __init__(self):
        self.cont = 1
        self.dic = {}
        self.visitados = {}
        self.clausulas = []
        self.fila = []
        self.certezas = [[-2]]

    def mostra_dic(self):
        print(self.dic)

    def enumera_casa(self, x, y):
        list = []
        chave = str(x) + '/' + str(y)
        if (chave in self.dic) == False:
            for i in range(2):
                list.append(self.cont)
                self.cont += 1
            self.dic.update({chave: list})

    def enumera_adj(self, x, y):
        self.enumera_casa(x, y+1)
        self.enumera_casa(x + 1, y)
        self.enumera_casa(x, y - 1)
        self.enumera_casa(x - 1, y)

    def sensores(self, x, y):
        chave = str(x) + '/' + str(y)
        lista = []
        if (chave in self.visitados) == False:
            dic = copy.deepcopy(self.dic)
            list = dic[chave]
            breeze = input("Tem Brisa? ")
            if breeze == "1":
                lista.append(list[0])
                self.clausulas.append(lista)
                return 1
            else:
                list[0] = int('-' + str(list[0]))
                lista.append(list[0])
                self.clausulas.append(lista)
                return 0

    def mostra_clausulas(self):
        for x in self.clausulas:
            print (x)

    def gera_clausulas(self, x, y):
        clausula = []
        dic = copy.deepcopy(self.dic)
        chave = str(x) + '/' + str(y)
        if (chave in self.visitados) == False:
            res = int("-" + str(dic[chave][0]))
            clausula.append(res)
            chave = str(x) + '/' + str(y + 1)
            clausula.append(dic[chave][1])
            chave = str(x + 1) + '/' + str(y)
            clausula.append(dic[chave][1])
            chave = str(x) + '/' + str(y - 1)
            clausula.append(dic[chave][1])
            chave = str(x - 1) + '/' + str(y)
            clausula.append(dic[chave][1])
            self.clausulas.append(clausula)

            clausula = []
            chave = str(x) + '/' + str(y)
            clausula.append(dic[chave][0])
            chave = str(x) + '/' + str(y + 1)
            res = int("-" + str(dic[chave][1]))
            clausula.append(res)
            self.clausulas.append(clausula)

            clausula = []
            chave = str(x) + '/' + str(y)
            clausula.append(dic[chave][0])
            chave = str(x + 1) + '/' + str(y)
            res = int("-" + str(dic[chave][1]))
            clausula.append(res)
            self.clausulas.append(clausula)

            clausula = []
            chave = str(x) + '/' + str(y)
            clausula.append(dic[chave][0])
            chave = str(x) + '/' + str(y - 1)
            res = int("-" + str(dic[chave][1]))
            clausula.append(res)
            self.clausulas.append(clausula)

            clausula = []
            chave = str(x) + '/' + str(y)
            clausula.append(dic[chave][0])
            chave = str(x - 1) + '/' + str(y)
            res = int("-" + str(dic[chave][1]))
            clausula.append(res)
            self.clausulas.append(clausula)

            chave = str(x) + '/' + str(y)
            self.visitados.update({chave : [x,y]})

    def posso_andar(self, xy):
        list = []
        dic = copy.deepcopy(self.dic)
        chave = str(xy[0]) + "/" + str(xy[1])
        s = Solver(name='g4')
        s.append_formula(self.clausulas)
        list.append(dic[chave][1])
        s.add_clause(list)
        print (s.solve())
        if s.solve() == False:
            list = []
            s = Solver(name='g4')
            s.append_formula(self.clausulas)
            dic[chave][1] = int("-" + str(dic[chave][1]))
            list.append(dic[chave][1])
            s.add_clause(list)
            res2 = s.solve()
            print (res2)
            if s.solve() == True:
                list = []
                chave = str(xy[0]) + "/" + str(xy[1])
                inverso = int("-" + str(self.dic[chave][1]))
                list.append(inverso)
                if (self.dic[chave][1] in self.certezas) == False:
                    self.clausulas.append(list)
                    self.certezas.append(dic[chave][1])
                return "livre"
            else:
                return "erro"
        else:
            list = []
            s = Solver(name='g4')
            s.append_formula(self.clausulas)
            dic[chave][1] = int("-" + str(self.dic[chave][1]))
            list.append(dic[chave][1])
            s.add_clause(list)
            res2 = s.solve()
            print(res2)
            if s.solve() == True:
                return "duvida"
            else:
                list = []
                chave = str(xy[0]) + "/" + str(xy[1])
                list.append(self.dic[chave][1])
                if (self.dic[chave][1] in self.certezas) == False:
                    self.clausulas.append(list)
                    self.certezas.append(dic[chave][1])
                return "poço"

    def libera_casa(self, x, y):
        list = []
        chave = str(x) + "/" + str(y)
        inverso = int("-" + str(self.dic[chave][1]))
        list.append(inverso)
        if (self.dic[chave][1] in self.certezas) == False:
            self.clausulas.append(list)
            self.certezas.append(self.dic[chave][1])

    def libera_adj(self, xy):
        x = xy[0]
        y = xy[1]
        self.libera_casa(x, y + 1)
        self.libera_casa(x + 1, y)
        self.libera_casa(x, y - 1)
        self.libera_casa(x-1, y)


    def pysat(self):
        s = Solver(name='g4')
        s.append_formula(self.clausulas)
        print (s.solve())
        for m in s.enum_models():
            print(m)
