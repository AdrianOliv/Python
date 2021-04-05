#Comprimento da hipotenusa a partir dos catetos.
from math import hypot
co = float(input('Valor do catedo oposto: '))
ca = float(input('Valor do cateto adjascente: '))
print(f'O valor da hipotenusa é {hypot(co,ca)}!')
