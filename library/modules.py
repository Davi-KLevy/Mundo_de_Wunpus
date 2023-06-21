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

    def vira(self, dir):
        if (dir - (self.direcao % 4) <= 4) and (dir - (self.direcao % 4) > 0):
            if self.direcao % 4 == 3:
                self.direcao = 0
            else:
                self.direcao = (self.direcao % 4) + 1
            print("r")
        elif (dir - (self.direcao % 4) >= -4) and (dir - (self.direcao % 4) < 0):
            if self.direcao % 4 == 0:
                self.direcao = 3
            else:
                self.direcao = (self.direcao % 4) - 1
            print("l")
     
    def andar_frente(self):
        if self.direcao % 4 == 1:
            self.y += 1
        elif self.direcao % 4 == 2:
            self.x += 1
        elif self.direcao % 4 == 3:
            self.y -= 1
        elif self.direcao % 4 == 0:
            self.x -= 1
        print ("m")
        print (f"LOCAL: {[self.x, self.y]}")
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
        
    def descubra_direcao(self, xy):
        if xy[0] == self.x:
            sub = xy[1] - self.y
            if sub > 0:
                return 1
            elif sub < 0:
                return 3
        elif xy[1] == self.y:
            sub = xy[0] - self.x
            if sub > 0:
                return 2
            elif sub < 0:
                return 0
        else:
            return 
        


class BancoDeDados:

    def __init__(self):
        self.cont = 1
        self.dic = {}
        self.visitados = []
        self.caminho = []
        self.caminho_volta = []
        self.clausulas_poco = []
        self.clausulas_wump = []
        self.bumps = []
        self.gold = 0
        self.scream = 0
        self.certezas_p = []
        self.certezas_w = []
        self.fila = []
        self.marca_duv = []

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
            dic2 = copy.deepcopy(self.dic)
            list = dic[chave]
            list_w = dic2[chave]
            senso = input()
            smell = senso[0]
            breeze = senso[1]
            glow = senso[2]
            bump = senso[3]
            scream = senso[4]

            self.caminho.insert(0, [x,y])
            
            if bump == "1":
                self.bumps.append(chave)
                self.caminho.pop(0)
                x = int(self.caminho[0][0])
                y = int(self.caminho[0][1])
            else:
                pass
            
            if breeze == "1":
                lista.append(list[0])
                self.clausulas_poco.append(lista)
            else:
                list[0] = int('-' + str(list[0]))
                lista.append(list[0])
                self.clausulas_poco.append(lista)


            lista = []
            if smell == "1":
                lista.append(list_w[0])
                self.clausulas_wump.append(lista)
            else:
                list_w[0] = int('-' + str(list_w[0]))
                lista.append(list_w[0])
                self.clausulas_wump.append(lista)


            if glow == "1":
                self.gold = 1
            else:
                pass

            if scream == "1":
                self.scream = 1
            else:
                pass

            return [smell, breeze]
        return

            
            

    def mostra_clausulas(self):
        for x in self.clausulas_poco:
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
            self.clausulas_poco.append(clausula)
            self.clausulas_wump.append(clausula)

            clausula = []
            chave = str(x) + '/' + str(y)
            clausula.append(dic[chave][0])
            chave = str(x) + '/' + str(y + 1)
            res = int("-" + str(dic[chave][1]))
            clausula.append(res)
            self.clausulas_poco.append(clausula)
            self.clausulas_wump.append(clausula)

            clausula = []
            chave = str(x) + '/' + str(y)
            clausula.append(dic[chave][0])
            chave = str(x + 1) + '/' + str(y)
            res = int("-" + str(dic[chave][1]))
            clausula.append(res)
            self.clausulas_poco.append(clausula)
            self.clausulas_wump.append(clausula)

            clausula = []
            chave = str(x) + '/' + str(y)
            clausula.append(dic[chave][0])
            chave = str(x) + '/' + str(y - 1)
            res = int("-" + str(dic[chave][1]))
            clausula.append(res)
            self.clausulas_poco.append(clausula)
            self.clausulas_wump.append(clausula)

            clausula = []
            chave = str(x) + '/' + str(y)
            clausula.append(dic[chave][0])
            chave = str(x - 1) + '/' + str(y)
            res = int("-" + str(dic[chave][1]))
            clausula.append(res)
            self.clausulas_poco.append(clausula)
            self.clausulas_wump.append(clausula)

            chave = str(x) + '/' + str(y)
            self.visitados.append(chave)

    def posso_andar(self, xy):
        poco = ""
        wumpus = ""
        list = []
        dic = copy.deepcopy(self.dic)
        chave = str(xy[0]) + "/" + str(xy[1])
        
        s = Solver(name='g4')
        s.append_formula(self.clausulas_poco)
        list.append(dic[chave][1])
        s.add_clause(list)
        #print (s.solve())
        if s.solve() == False:
            list = []
            s = Solver(name='g4')
            s.append_formula(self.clausulas_poco)
            dic[chave][1] = int("-" + str(dic[chave][1]))
            list.append(dic[chave][1])
            s.add_clause(list)
            res2 = s.solve()
            #print (res2)
            if s.solve() == True:
                list = []
                chave = str(xy[0]) + "/" + str(xy[1])
                inverso = int("-" + str(self.dic[chave][1]))
                list.append(inverso)
                if (self.dic[chave][1] in self.certezas_p) == False:
                    self.clausulas_poco.append(list)
                    self.certezas_p.append(dic[chave][1])
                poco = "livre"
            else:
                poco = "erro"
        else:
            list = []
            s = Solver(name='g4')
            s.append_formula(self.clausulas_poco)
            dic[chave][1] = int("-" + str(self.dic[chave][1]))
            list.append(dic[chave][1])
            s.add_clause(list)
            res2 = s.solve()
            #print(res2)
            if s.solve() == True:
                poco = "duvida"
            else:
                list = []
                chave = str(xy[0]) + "/" + str(xy[1])
                list.append(self.dic[chave][1])
                if (self.dic[chave][1] in self.certezas_p) == False:
                    self.clausulas_poco.append(list)
                    self.certezas_p.append(dic[chave][1])
                poco = "morte"




        list = []
        dic = copy.deepcopy(self.dic)
        chave = str(xy[0]) + "/" + str(xy[1])
        
        s = Solver(name='g4')
        s.append_formula(self.clausulas_wump)
        list.append(dic[chave][1])
        s.add_clause(list)
        #print (s.solve())
        if s.solve() == False:
            list = []
            s = Solver(name='g4')
            s.append_formula(self.clausulas_wump)
            dic[chave][1] = int("-" + str(dic[chave][1]))
            list.append(dic[chave][1])
            s.add_clause(list)
            res2 = s.solve()
            #print (res2)
            if s.solve() == True:
                list = []
                chave = str(xy[0]) + "/" + str(xy[1])
                inverso = int("-" + str(self.dic[chave][1]))
                list.append(inverso)
                if (self.dic[chave][1] in self.certezas_w) == False:
                    self.clausulas_wump.append(list)
                    self.certezas_w.append(dic[chave][1])
                wumpus = "livre"
            else:
                wumpus = "erro"
        else:
            list = []
            s = Solver(name='g4')
            s.append_formula(self.clausulas_wump)
            dic[chave][1] = int("-" + str(self.dic[chave][1]))
            list.append(dic[chave][1])
            s.add_clause(list)
            res2 = s.solve()
            #print(res2)
            if s.solve() == True:
                wumpus = "duvida"
            else:
                list = []
                chave = str(xy[0]) + "/" + str(xy[1])
                list.append(self.dic[chave][1])
                if (self.dic[chave][1] in self.certezas_w) == False:
                    self.clausulas_wump.append(list)
                    self.certezas_w.append(dic[chave][1])
                wumpus = "morte"

        juntos = [poco, wumpus]
        if juntos[0] == "duvida" or juntos[1] == "duvida":
            if self.marca_duv == []:
                self.marca_duv = xy
            if ((xy in self.fila) == True):
                self.fila.remove(xy)
                self.fila.append(xy)
                print (self.fila)
            elif (xy in self.fila) == False:
                self.fila.append(xy)
                self.marca_duv = xy
            return "nao pode andar"
        elif juntos[0] == "morte" or juntos[1] == "morte":
            self.fila.remove(xy)
            return "nao pode andar"
        elif juntos == ["livre", "livre"]:
            self.fila.pop(0)
            return "pode andar" 

    def libera_casa(self, x, y, tipo):
        list = []
        chave = str(x) + "/" + str(y)
        
        if tipo == "Poco":
            inverso = int("-" + str(self.dic[chave][1]))
            list.append(inverso)
            if (self.dic[chave][1] in self.certezas_p) == False:
                self.clausulas_poco.append(list)
                self.certezas_p.append(inverso)

        elif tipo == "Wumpus":
            inverso = int("-" + str(self.dic[chave][1]))
            list.append(inverso)
            if (self.dic[chave][1] in self.certezas_w) == False:
                self.clausulas_wump.append(list)
                self.certezas_w.append(inverso)

    def libera_adj(self, xy, tipo):
        x = xy[0]
        y = xy[1]
        self.libera_casa(x, y + 1, tipo)
        self.coloque_na_fila(x,y + 1)
        self.libera_casa(x + 1, y, tipo)
        self.coloque_na_fila(x + 1,y)
        self.libera_casa(x, y - 1, tipo)
        self.coloque_na_fila(x,y - 1)
        self.libera_casa(x-1, y, tipo)
        self.coloque_na_fila(x - 1,y)


    def coloque_na_fila(self, x ,y):
        chave = [x,y] 
        chave_str = str(x) + '/' + str(y)
        if ((chave_str in self.visitados) == False) and ((chave in self.fila) == False):
            self.fila.append(chave)
    
    def pysat(self):
        s = Solver(name='g4')
        s.append_formula(self.clausulas_poco)
        print (s.solve())
        for m in s.enum_models():
            print(m)


    def calcula_distancia(self, xy):
        distancia = abs(xy[0] - self.fila[0][0]) + abs(xy[1] - self.fila[0][1])
        return distancia
    
    def descobre_caminho(self):
        self.caminho_volta = []
        cont = 0
        cont2 = 0
        
        for casa in self.caminho:
            adj = abs(casa[0] - self.fila[0][0]) + abs(casa[1] - self.fila[0][1])
            if adj == 1:
                salva_casa = casa
                break

        for casa in self.caminho:
            if casa == salva_casa:
                self.caminho_volta.append(casa)
                break
            elif cont > 0:
                self.caminho_volta.append(casa)
            cont += 1
        
        #print ("antes")
        #print (self.caminho_volta)
        
        try:
            while self.caminho_volta.count(self.caminho[0]) != 0:
                aux = self.caminho_volta.index(self.caminho[0])

                if aux == 0:
                    pass
                else:
                    #print(aux)
                    for i in range(aux + 1):
                        self.caminho_volta.pop(0)
        except:
            pass

        #print ("depois")
        #print (self.caminho_volta)

        #teste = input("teste")

        caminho_volta = self.caminho_volta
        for casa in caminho_volta:
            while True:    
                if caminho_volta.count(casa) > 1:
                    #print ("Conta casas")
                    #print (caminho_volta.count(casa))
                    ponto1 = caminho_volta.index(casa)
                    #print (ponto1)
                    ponto2 = caminho_volta.index(casa, ponto1+1)
                    #print (ponto2)
                    if ponto2 - ponto1 == 1:
                        break
                    for i in range(ponto2 + 1):
                        if i > ponto1 and i <= ponto2:
                            #print(caminho_volta)
                            #print(i)
                            caminho_volta.pop(1)
                else:
                    break
        self.caminho_volta = caminho_volta
        cont2 += 1
        #print (f"Iteração: {cont2}")
        #print (self.caminho_volta )
        #print (self.caminho)

    def mostra_tudo(self, x, y):
        #print(f"\nLOCAL: [{x}/{y}]\n")
        print(f"DIC Poço: {self.dic}\n")
        print(f"Bumps: {self.bumps}\n Ouro: {self.gold}\n Grito: {self.scream}")
        print(f"CAMINHO: {self.caminho}\nVISITADOS: {self.visitados}\n")
        print(f"Certezas Poco: {self.certezas_p}\n Certezas Wumpus: {self.certezas_w}")
        print(f"Marca Duvida: {self.marca_duv}")
        #print(f"Claus. Poco: {self.clausulas_poco}\nClaus. Wumpus: {self.clausulas_wump}")
        print(f"Fila: {self.fila}")
