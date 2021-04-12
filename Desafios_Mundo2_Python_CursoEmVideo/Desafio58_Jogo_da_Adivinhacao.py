# Melhorando desafio 28 - PC pensa em um numero de 0 a 10
# Finalizar somente quando usuario acertar e mostrar tentativas
from random import randint
print('=-' * 20)
print('{:^40}'.format('JOGO DA ADIVINHACAO'))
print('=-' * 20)
pc = randint(1, 10)
usu = 0
tent = 0
print('De 0 a 10...')
print('Adivinhe em qual número estou pensando: ')
while usu != pc:
    usu = int(input('... '))
    tent += 1
print('\033[32mVOCÊ ACERTOU!\033[m')
print(f'Você tentou {tent} vezes até acertar!')
