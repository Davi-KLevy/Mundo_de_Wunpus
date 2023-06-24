from library.modules import *

banco = BancoDeDados()
comput = Jogador()


def workspace():
    xy = [0, 0]
    banco.enumera_casa(xy[0], xy[1])
    banco.enumera_adj(xy[0], xy[1])
    aux = banco.sensores(xy[0], xy[1])
    banco.libera_casa(xy[0], xy[1], "Poco")
    banco.libera_casa(xy[0], xy[1], "Wumpus")
    if aux == ["0","0"]:
        banco.libera_adj(xy, "Poco")
        banco.libera_adj(xy, "Wumpus")
    elif aux == ["0","1"]:
        banco.libera_adj(xy, "Wumpus")
    elif aux == ["1","0"]:
        banco.libera_adj(xy, "Poco")
    banco.gera_clausulas(xy[0], xy[1])
    #banco.mostra_tudo(xy[0], xy[1])
    while True:
        try:
            for pos in banco.bumps:
                if (pos in banco.fila) == True:
                    banco.fila.remove(pos)
        except:
            pass
        
        
        if banco.gold == 1:
            print("p")
            banco.gold = 2
        
        if banco.wumpus != [0]:
            res = banco.alinhado_wumpus(xy)
            if res == "sim":
                while banco.flecha != 0:
                    dir = comput.descubra_direcao(banco.wumpus, xy)
                    if (dir % 4) == (comput.direcao % 4):
                        #print(f"Eu, estando no local {xy} atirei a flecha na direcao {comput.direcao}.")
                        print("s")
                        banco.fila.insert(0, banco.wumpus)
                        aux = banco.sensores(xy[0], xy[1])
                        banco.flecha = 0
                    elif (dir % 4) != (comput.direcao % 4):
                        comput.vira(dir)
        
        if banco.gold == 2:
            print("e")
            break
        elif banco.fila == []:
            print("e")
            break

        elif banco.marca_duv == banco.fila[0]:
            if banco.flecha == 0:
                print("e")
                break
            else:
                #print(f"Eu, estando no local {xy} atirei a flecha na direcao {comput.direcao}.")
                print("s")
                banco.marca_duv = []
                frente = comput.retorna_frente()

                list = []
                chave = str(frente[0]) + "/" + str(frente[1])
                inverso = int("-" + str(banco.dic[chave][1]))
                list.append(inverso)
                banco.clausulas_wump.append(list)
                banco.certezas_w.append(inverso)

                banco.fila.remove(frente)
                banco.fila.insert(0, frente)
                aux = banco.sensores(xy[0], xy[1])
                banco.flecha = 0
                
        
        elif banco.gold == 0 and banco.marca_duv != banco.fila[0]:
            dis = banco.calcula_distancia(xy)
            if dis == 1:
                dir = comput.descubra_direcao(banco.fila[0], xy)
                #print (f"{dir} - {comput.direcao}")
                if (dir % 4) == (comput.direcao % 4):
                    frente = comput.retorna_frente()
                    res = banco.posso_andar(frente)
                    #print (res)
                    if res == "pode andar":
                        comput.andar_frente()
                        banco.marca_duv = []
                        xy = [comput.x, comput.y]
                        banco.enumera_casa(xy[0], xy[1])
                        banco.enumera_adj(xy[0], xy[1])
                        aux = banco.sensores(xy[0], xy[1])
                        bump = xy
                        xy = banco.caminho[0]
                        banco.gera_clausulas(xy[0], xy[1])
                        list = [xy]
                        if (list in banco.visitados) == False:   
                            #print("achou")
                            if aux == ["0","0"]:
                                banco.libera_adj(xy, "Poco")
                                banco.libera_adj(xy, "Wumpus")
                            elif aux == ["0","1"]:
                                banco.libera_adj(xy, "Wumpus")
                            elif aux == ["1","0"]:
                                banco.libera_adj(xy, "Poco")
                        #banco.mostra_tudo(xy[0], xy[1])
                    else:
                        pass
                elif (dir % 4) != (comput.direcao % 4):
                    comput.vira(dir)
                    inp = input()
                    #aux = banco.sensores(xy[0], xy[1])
            elif dis != 1:
                #print (dis)
                #print (banco.fila)
                banco.descobre_caminho()
                dir = comput.descubra_direcao(banco.caminho_volta[0], xy)
                #print (f"{dir} - {comput.direcao}")
                if (dir % 4) == (comput.direcao % 4):
                    comput.andar_frente()
                    inp = input()
                    banco.marca_duv = []
                    xy = [comput.x, comput.y]
                    banco.caminho.insert(0, [xy[0],xy[1]])
                    banco.caminho_volta.pop(0)
                elif (dir % 4) != (comput.direcao % 4):
                    comput.vira(dir)
                    inp = input()
                    #aux = banco.sensores(xy[0], xy[1])

                




if __name__ == '__main__':
    workspace()
