# Programa com duas funcoes
# uma de sorteio e outra de soma de pares.

from random import randint

def sortear():
    l = []
    for i in range(5):
        l.append(randint(1,100))
    return l

def pares(lista):
    print(f"\nOs númeroes pares da lista são: ", end ="")
    for i in lista:
        if i % 2 == 0:
            print(i, end=" ")
        
lista = list()
lista = sortear()
print(f"\nOs números sorteados foram: {lista}")
pares(lista)
