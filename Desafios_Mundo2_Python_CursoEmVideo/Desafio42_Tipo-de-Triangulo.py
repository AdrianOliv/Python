# Dizer que tipo de triangulo é.
a = int(input('Valor da primeira reta: '))
b = int(input('Valor da segunda reta: '))
c = int(input('Valor da terceira reta: '))
if a<(b+c) and b<(a+c) and c<(a+b):
    print('\033[34mO triangulo PODE SER FORMADO a partir destas retas!\033[m')
else:
    print('\033[31mO triangulo NÃO PODE ser formado!')

if a == b and b==c :
    print('TRIANGULO EQUILÁTERO.\n')
elif a != b and b != c :
    print('TRIANGULO ESCALENO.\n')
else :
    print('TRIANGULO ISÓSCELES.\n')
