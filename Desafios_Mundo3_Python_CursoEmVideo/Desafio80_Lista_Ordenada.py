# Programa que lê cinco números digitados.
# Ordenar lista sem o sort.

l = []
for i in range(5):
    num = int(input("\nDigite um número: "))
    if l == []:
        l.append(num)
        print('Primeira Adição.')
    else:
        for c, v in enumerate(l):
            if num <= v:
                l.insert(c, num)
                print(f'Inserido na posição {c}.')
                break
            elif c+1 == len(l):
                l.append(num)
                print(f'Adicionado na posição {l.index(num)}.')
                break

print(f'\n\033[32mOs números que você digitou foram: {l}\033[m')
