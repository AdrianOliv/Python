from Funcoes_Jogo import *
from time import sleep

cartas = cartoes()

while True:
    if play():
        # Inicio
        for carta in cartas:
            titulo()
            print('\nOlhe com atenção para a tabela abaixo...\n')
            sleep(2)
            mostra_carta(carta)
            print('\n')
            # função idade
            sleep(5)

        # Fim
    else:
        fim()
        break
