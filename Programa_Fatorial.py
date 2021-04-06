# Criação de um programa de fatorial.
from math import factorial
def fat(x):
     if x <= 1:
         print('\033[34mO fatorial de 1 e 0 é igual a: 1\033[m')
     else:
         for i in range(x-1, 0, -1):
             x = x * i
         print(f'\033[32mO fatorial é: {x}\033[m')
            
var = int(input('Digite o num: '))
fat(var)

# Pela função interna.
print(factorial(var))

# Exemplo pego na internet
def fact(num):
# Primeiro if adicionado posteriormente
    if num == 0:
        return 1
    elif num == 1:
        return num
    else:
        return num * fact(num-1)

print(fact(var))
