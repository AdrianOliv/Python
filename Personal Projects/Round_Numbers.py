# Um programa em que o usuário insira um número.
# Deve imprimir Pi com esse número de casas decimais.
# Tentar manter um limite de quão longe o programa irá.

from math import pi
while True:
    n = int(input("Quantos n° decimais: "))
    if n > 10:
        print("Valor não permitido!")
    else:
        print(round(3.1415926535, n))
    
    o = input("Continuar(y/n): ")
    if o in "Nn":
        break
