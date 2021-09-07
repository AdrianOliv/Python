# Begin
from time import sleep
from ModulosCeV import Mod_Moeda

def titulo():
    print('========  CALCULO FINANCEIRO  ========')

def fim():
    print('======== PROGRAMA FINALIZADO ========')
    sleep(2)


# Main
titulo()
print(Mod_Moeda.moeda(Mod_Moeda.aumentar(1500, 10)))
print(Mod_Moeda.moeda(Mod_Moeda.diminuir(1500, 10)))
print(Mod_Moeda.moeda(Mod_Moeda.dobro(80)))
print(Mod_Moeda.moeda(Mod_Moeda.metade(90)))
fim()