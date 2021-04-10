# Programa de PA com primeiro termo 3 razao.
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao da PA: '))
num = 0
for i in range(termo, 1000, razao):
    num += 1
    print(i)
    if num == 10:
        break
