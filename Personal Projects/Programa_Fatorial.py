# Programa Fatorial.
# Importando Biblioteca
from math import factorial

# Exemplo pesquisado
def fact(num):
# Primeiro if adicionado posteriormente
    if num == 0:
        return 1
    elif num == 1:
        return num
    else:
        return num * fact(num-1)

# Definindo uma função
def fat(x):
     if x <= 1:
         return 1
     else:
         for i in range(x-1, 0, -1):
             x = x * i
         return x
            
num = int(input('Digite o num: '))

print("\nPela função definida")
print(fat(num))

print("\nPela função do import math.")
print(factorial(num))

print('\nPela função pesquisada')
print(fact(num))
