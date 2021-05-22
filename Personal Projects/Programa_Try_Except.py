# Usando Try e Except com factorial
from math import factorial
try:
    x = 1
    while x > 0:
        x = int(input('Digite um número(0 para sair):  '))
        print(factorial(x))
except:
    print('Você finalizou!')
