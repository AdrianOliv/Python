# Ler 3 retas e dizer se podem formar um triangulo.
# Regra
#   b-c < a < b+c
#   a-c < b < a+c
#   a-b < c < a+b
a = int(input('Valor da primeira reta: '))
b = int(input('Valor da segunda reta: '))
c = int(input('Valor da terceira reta: '))
if a<(b+c) and b<(a+c) and c<(a+b):
    print('O triangulo PODE SER FORMADO a partir destas retas!')
else:
    print('O triangulo NÃO PODE ser formado!')
