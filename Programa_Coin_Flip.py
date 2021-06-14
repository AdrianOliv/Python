# Coin Flip
from random import randint
moeda = ("Cara", "Coroa")

while True:
    print(moeda[randint(0,1)])
    
    while True:
        o = input("Continuar(y/n): ")
        if o in "YyNn":
            print()
            break
        else:
            print("\033[31mValor Inválido.\033[m")
    if o in "Nn":
        break
