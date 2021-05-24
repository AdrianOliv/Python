# Ler vários números e colocar em uma lista.
# Dizer quantos números foram digitados
# Lista em ordem decrescente
# Se o valor 5 está na lista

l = []
while True:
    num = int(input("Digite um número: "))
    l.append(num)

    while True:
        op = input("Continuar(y/n): ")
        if op == 'y' or op == 'n':
            break
        else:
            print('Valor inválido!')
    if op == 'n':
        break

print(f'\nVocê digitou {len(l)} números.')
print(f'Na ordem decrescente fica: {sorted(l, reverse = True)}')

if 5 in l:
    print('Você digitou {} vezes o número 5.'.format(l.count(5)))
else:
    print('Você não digitou o número 5.')
