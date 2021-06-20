# Programa de PA com primeiro termo e razao.
# Agora utilizando while.
# Agora com loop até 0 termos.
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao da PA: '))
num = 0
pa = termo
i = 10
while i != 0:
    while num != i:
        print(pa)
        pa += razao
        num += 1
    i = int(input('Mais quantos: '))
    num = 0
