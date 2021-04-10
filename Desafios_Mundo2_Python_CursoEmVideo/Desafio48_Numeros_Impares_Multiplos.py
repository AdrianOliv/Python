# Criar um programa que some os impares multiplos de 3
soma = 0
for i in range(1, 500, 2):
    if i % 3 == 0:
        soma += i
print('A soma é {}'.format(soma))
