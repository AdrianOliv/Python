# Melhoria do Desafio 86.
# Adicionar soma dos pares, soma da terceira
# coluna e maior valor da segunda linha.

s = sp = 0
k = 1
m = [[], [], []]

for i in range(3):
    for j in range(3):
        m[i].append(int(input(f"- {k}° valor: ")))
        k += 1
        if m[i][j] % 2 == 0:
            sp += m[i][j]
        if j == 2:
            s += m[i][j]
        
for i in range(3):
    print("\n")
    for j in range(3):
        print(f'|{m[i][j]:^5}|', end = "")

print(f'\n\nA soma dos pares é: {sp}.')
print(f'A soma da 3° coluna é: {s}.')
print(f'O maior da 2° linha é: {max(m[1])}.')
