# Criar uma tupla com 5 numeros aleatórios, 20
# Mostrar a tupla e dizer quais sao os numeros menores e maiores.
from random import randint

tupla = ()
for i in range(5):
    tupla = tupla + ((randint(0, 100)), )

print("\033[35m\nOs valores adicionado foram {}.".format(tupla))
print("O Menor valor foi {}.".format(sorted(list(tupla))[0]))
print("O Maior valor foi {}.\n\033[m".format(sorted(list(tupla))[4]))
