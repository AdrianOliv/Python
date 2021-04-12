# Programa que lê um número e mostra o seu fatorial.
n = int(input('Digite um número: '))
f = 1
for i in range(n, 0, -1):
    f = f * i
print(f'O fatorial de {n}! é {f}')

# Usando o while.
i = n
f = 1
while i != 0:
    f = f * i
    i -= 1
print(f'O fatorial de {n}! é {f}')
