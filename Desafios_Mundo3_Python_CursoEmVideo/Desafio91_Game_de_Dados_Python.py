# Criar 4 jogadores e sortear dados para cada um.
# Guardar resultados em um dicionário.
# Organizar o dicionário e mostrar vencedor com maior número.

from random import randint
from time import sleep

Jogo = {}
for i in range(4):
    dd = randint(1,6)
    jog = (f'jogador {i+1}')
    print(f'O {jog} tirou {dd}')
    Jogo[jog] = dd
    sleep(1.1)



    ################# IMCOMPLETO ####################