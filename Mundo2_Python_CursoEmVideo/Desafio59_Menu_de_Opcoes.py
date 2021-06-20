# Programa que lê dois valores e mostra ao usuario 4 opcoes e sair do programa.
import os
from time import sleep
print('=-' * 20)
print('{:^40}'.format('CALCULADORA'))
print('=-' * 20)
i = 4
while i != 5:
    if i == 1:
        print(f'\nA soma dos dois números é \033[32m{n1+n2}\033[m!')
    elif i == 2 :
        print(f'\nO produto dos números é \033[32m{n1*n2}\033[m!')
    elif i == 3 :
        if n1 > n2:
            print(f'\nO número \033[32m{n1}\033[m é maior!')
        else:
            print(f'\nO número \033[32m{n2}\033[m é maior!')
    elif i == 4 :
        n1 = float(input('\nDigite primeiro numero: '))
        n2 = float(input('Digite segundo numero: '))
    else:
        print('\033[31mOpção incorreta... \033[m')
    
    sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    i = int(input(f'''
[1] - SOMAR
[2] - MULTIPLICAR
[3] - MAIOR
[4] - NOVOS NÚMEROS
[5] - SAIR DO PROGRAMA

Seus números são \033[32m{n1}\033[m e \033[32m{n2}\033[m. Digite a sua opção: '''))

print('\n\033[31mPROGRAMA FINALIZADO\033[m')
