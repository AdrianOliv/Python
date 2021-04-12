# Programa de PA com primeiro termo e razao.
# Agora utilizando while.
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao da PA: '))
num = 0
pa = termo
while num != 10:
    print(pa)
    pa += razao
    num += 1
