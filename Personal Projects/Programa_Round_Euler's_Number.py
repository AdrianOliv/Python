# Desenvolva um programa em que o usuário insira um número.
# Seu programa deve imprimir 'e' até essa quantidade de casas decimais.
# Mantenha um limite de quão longe o programa irá.

from math import exp
while True:
    i = int(input("Qtd de Digitos: "))
    if i > 15:
        print("Valor não permitido!")
    else:
        print(round(exp(1), i))
    
    o = input("Continue(y/n): ")
    print()
    if o in "Nn":
        break
