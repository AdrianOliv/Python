# Criar 4 jogadores e sortear dados para cada um.
# Guardar resultados em um dicionário.
# Organizar o dicionário e mostrar vencedor com maior número.

from random import randint
from time import sleep
from operator import itemgetter

Jogo = {}
Ranking = {}
for i in range(4):
    dd = randint(1,6)
    jog = (f'Jogador {i+1}')
    print(f'O {jog} tirou {dd}.')
    Jogo[jog] = dd
    sleep(1.1)

print('-' * 40)
Ranking = sorted(Jogo.items(), key = itemgetter(1), reverse = True)
for i in Ranking:
    print(f'O {i[0]} tirou {i[1]}.')