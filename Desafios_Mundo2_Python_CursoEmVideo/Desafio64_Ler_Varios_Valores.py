# Programa que lê os numeros ate digitar 999.
# quantos foram digitados e a soma deles.
num = soma = digi = 0
while num != 999:
    soma += num
    digi += 1
    num = int(input('Diga um número: '))
else:
    print(f'\nForam lidos {digi-1} números.')
    print(f'A soma deu {soma}')
    print('\033[31mPrograma Finalizado!\033[m\n')
