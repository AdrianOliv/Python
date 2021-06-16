# Usando Try e Except com factorial
# A função try é excelente para evitar erros de programa que,
# principalmente quando o usuário erro o tipo de entrada.

from math import factorial
try:
    x = int(input('Digite um número:  '))
    print(factorial(x))
except:
    # Se usuário digitar uma str ou float
    print('Valor Inválido')