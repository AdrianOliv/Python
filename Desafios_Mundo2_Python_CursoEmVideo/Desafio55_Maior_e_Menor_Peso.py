# Programa que lê o menor e o maior peso digitado.
# Obs: o programa não pode reconhecer seguidamente itens menores ou maiores.
me_peso = 1000
ma_peso = 0
for i in range(5):
    peso = float(input(f'Pessoa {i+1}, digite seu peso: '))
    if peso < me_peso:
        me_peso = peso
    elif peso > ma_peso:
        ma_peso = peso
print('O maior peso foi: {}'.format(ma_peso))
print('O menor peso foi: {}'.format(me_peso))

# Outro jeito, usando listas.
# Obs: usando a list, usamos mais memória, de acordo que a
lista = []
for i in range(5):
    peso = float(input('Digite o peso: '))
    lista.append(peso)
lista.sort()
print(f'O maior peso foi: {lista[4]}')
print('O menor peso foi: {}'.format(lista[0]))
