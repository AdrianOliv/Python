# Begin
from time import sleep
from Mod_Moeda import *

def titulo():
    print('========  CALCULO FINANCEIRO  ========')

def moeda(x):
    return f'R$ {x}'

def fim():
    print('======== PROGRAMA FINALIZADO ========')
    sleep(2)


# Main
titulo()
print(moeda(aumentar(1500, 10)))
print(moeda(diminuir(1500, 10)))
print(moeda(dobro(80)))
print(moeda(metade(90)))
fim()