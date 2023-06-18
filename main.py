from library.modules import *

banco = BancoDeDados()
comput = Jogador()


def workspace():
    xy = [0, 0]
    banco.enumera_casa(xy[0], xy[1])
    aux = banco.sensores( xy[0],xy[1])
    if aux == 0:
        banco.clausulas.append([-2])
    banco.enumera_adj( xy[0],xy[1])
    banco.gera_clausulas(xy[0], xy[1])
    if aux == 1:
        res = banco.posso_andar([0,1])
    elif aux == 0:
        res = banco.libera_adj(xy)
    while True:
        print("""O QUE VOCÊ QUER FAZER? 
1) Andar pra frente
2) Vira Direita
3) Vira Esquerda
4) Mostra Clausulas
5) Fecha Programa\n""")
        res = input("Resposta: ")
        if res == "0":
            banco.mostra_dic()
        elif res == "1":
            xy = comput.andar_frente()
            banco.enumera_adj(xy[0], xy[1])
            aux = banco.sensores(xy[0], xy[1])
            if aux == 0:
                res = banco.libera_adj(xy)
            banco.gera_clausulas(xy[0], xy[1])
        elif res == "2":
            comput.vira_direita()
        elif res == "3":
            comput.vira_esquerda()
        elif res == "4":
            banco.mostra_clausulas()
        elif res == "5":
            break
        elif res == "6":
            frente = comput.retorna_frente()
            print (frente)
            res = banco.posso_andar(frente)
            print (res)
        elif res == "10":
            banco.pysat()


if __name__ == '__main__':
    workspace()
