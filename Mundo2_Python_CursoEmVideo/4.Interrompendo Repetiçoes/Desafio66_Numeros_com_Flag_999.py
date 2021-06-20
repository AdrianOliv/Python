# Ler vários números interiros e parar com 999.
# Contar quantos digitados e a soma deles.

s = i = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    s += num
    i += 1

print(f'\nForam digitados {i} números.')
print(f'A soma dos números foi: {s}.')
print('Finalizado!')
