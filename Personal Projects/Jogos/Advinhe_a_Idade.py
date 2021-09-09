import Funcoes_Jogo

cartas = Funcoes_Jogo.cartoes()
while True:
    if Funcoes_Jogo.play():
        print('jogando')
    else:
        break