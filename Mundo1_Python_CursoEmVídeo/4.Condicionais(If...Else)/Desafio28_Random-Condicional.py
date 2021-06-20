# Fazer o computador escolher um número de 1 a 5 e deixar usuário
# tentar acertar.
from random import randint
from time import sleep
num = randint(1, 5)
print('-=-' * 20)
print('Vou pensar em um número, tente adivinhar!')
print('-=-' * 20)
num_usuario = int(input('De 1 a 5, escolha um número: '))
print('PROCESSANDO...')
sleep(1)
if num_usuario == num :
    print('\033[1;32mVocê Acertou!\033[m')
else:
    print(f'\033[31mVocê errou, o núm certo era: {num}\033[m')
