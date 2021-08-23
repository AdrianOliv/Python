# Begin
from time import sleep

def fatorial(n=1, show=0):
    f = 1
    for i in range(n, 0, -1):
        f = f * i
        if show == 1:
            print(f, end=" ", flush=True)
            sleep(2)
    print(f'\nO fatorial {n}! é {f}')


# Main
n = int(input('Digite um número: '))

# Mostrando numeros
fatorial(n,1)

# Sem mostrar números
fatorial(n)
