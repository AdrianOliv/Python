# Programa que lê entrada de usuário em uma lista
# Se o número digitado já houver, não é adicionado
# Mostrar valores em ordem crescente.

l = []
for i in range(6):
    num = int(input("Digite um número: "))
    if num not in l:
        l.append(num)

print(f'Os números digitados foram {sorted(l)}.')
