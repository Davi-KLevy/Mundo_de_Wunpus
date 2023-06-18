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
    if aux == [0,0]:
        banco.libera_adj(xy, "Poco")
        banco.libera_adj(xy, "Wumpus")
    elif aux == [0,1]:
        banco.libera_adj(xy, "Wumpus")
    elif aux == [1,0]:
        banco.libera_adj(xy, "Poco")
    banco.gera_clausulas(xy[0], xy[1])
    banco.mostra_tudo(xy[0], xy[1])




if __name__ == '__main__':
    workspace()
