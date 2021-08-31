# Begin
from time import sleep
from ModulosCeV import Mod_Moeda
from os import system

def titulo():
    print('========  CALCULO FINANCEIRO  ========')
    print('Digite "9999" para finalizar.\n')
    
    
def calculo(x):
    print('''
    Selecione uma das opções abaixo:
    1 - aumentar       2 - diminuir
    3 - dobrar         4 - metade
    ''')
    o = 0
    while str(o) not in '1234':
        o = int(input('Qual a sua opção: '))
    if str(o) in '12':
        y = int(input('Digite o percentual a ser usado: '))
    print('O valor é R$ ', end = '')
    if o == 1:
        print(Mod_Moeda.aumentar(x, y))
    elif o == 2:
        print(Mod_Moeda.diminuir(x, y))
    elif o == 3:
        print(Mod_Moeda.dobro(x))
    else:
        print(Mod_Moeda.metade(x))
    sleep(2)

def fim():
    print('======== PROGRAMA FINALIZADO ========')
    sleep(2)


# Main
while True:
    system('cls')
    titulo()
    x = float(input('Digite o valor a ser calculado.\nR$ '))
    if x == 9999:
        break
    else:
        calculo(x)
fim()