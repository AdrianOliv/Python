# Criar programa que jogue Jokenpô.
# Criar random de 1 a 3 sendo:
#   1 - Pedra
#   2 - Papel
#   3 - Tesoura
from random import randint
from time import sleep
import os
usu = 1
while usu != 99 :
    # Cabeçalho:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-=' * 20)
    print('{:^40}'.format('VAMOS JOGAR JOKENPÔ!'))
    print('-=' * 20)
    print('''Escolha uma das opões abaixo: 
        1 - Pedra
        2 - Papel
        3 - Tesoura\n ''')

    # Variáveis:
    op = ["Pedra", "Papel", "Tesoura"]
    pc = randint(1,3)
    usu = int(input('Digite a sua opção: '))
    
    if usu > 0 and usu < 4:
        print(f'O PC escolheu \033[32m{op[pc-1]}\033[m e você \033[32m{op[usu-1]}\033[m!')
        if (pc - usu) == 1 or (usu - pc) == 2:
            print('\033[31mVOCÊ PERDEU!\033[m\n')
        elif pc == usu :
            print('\033[34mVOCÊS EMPATARAM!\033[m\n')
        else:
            print('\033[32mVOCÊ GANHOU!\033[m\n')
    else:
        print('Opção Inválida!\n')

    print('Processando...')
    sleep(3)
else:
    print('FIM DE JOGO!')
    sleep(3)
