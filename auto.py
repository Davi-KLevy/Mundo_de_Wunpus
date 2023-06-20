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
    banco.mostra_tudo(xy[0], xy[1])
    while True:
        if banco.scream == 1:
            pass
        if banco.gold == 1:
            print("p")
        
        elif banco.fila == []:
            print("e")
            break

        elif banco.marca_duv == banco.fila[0]:
            print("e")
            break
        
        elif banco.gold == 0 and banco.marca_duv != banco.fila[0]:
            dis = banco.calcula_distancia(xy)
            if dis == 1:
                dir = comput.descubra_direcao(banco.fila[0])
                print (f"{dir} - {comput.direcao}")
                if (dir % 4) == (comput.direcao % 4):
                    frente = comput.retorna_frente()
                    res = banco.posso_andar(frente)
                    print (res)
                    if res == "pode andar":
                        comput.andar_frente()
                        print("1")
                        xy = [comput.x, comput.y]
                        banco.enumera_casa(xy[0], xy[1])
                        banco.enumera_adj(xy[0], xy[1])
                        aux = banco.sensores(xy[0], xy[1])
                        banco.gera_clausulas(xy[0], xy[1])
                        print("1")
                        banco.mostra_tudo(xy[0], xy[1])
                        if aux == ["0","0"]:
                            banco.libera_adj(xy, "Poco")
                            banco.libera_adj(xy, "Wumpus")
                        elif aux == ["0","1"]:
                            banco.libera_adj(xy, "Wumpus")
                        elif aux == ["1","0"]:
                            banco.libera_adj(xy, "Poco")
                    else:
                        pass
                elif (dir % 4) != (comput.direcao % 4):
                    comput.vira(dir)
                    #aux = banco.sensores(xy[0], xy[1])
            elif dis != 1:
                print (dis)
                #print (banco.fila)
                banco.descobre_caminho()
                dir = comput.descubra_direcao(banco.caminho_volta[0])
                #print (f"{dir} - {comput.direcao}")
                if (dir % 4) == (comput.direcao % 4):
                    comput.andar_frente()
                    xy = [comput.x, comput.y]
                    banco.caminho.insert(0, [xy[0],xy[1]])
                    banco.caminho_volta.pop(0)
                elif (dir % 4) != (comput.direcao % 4):
                    comput.vira(dir)
                    #aux = banco.sensores(xy[0], xy[1])

                




if __name__ == '__main__':
    workspace()
