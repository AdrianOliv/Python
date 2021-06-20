# Programa que lê 5 valores em lista.
# Mostrar o maior e o menor e as suas posições.

n = [int(input("Digite um número: ")),
     int(input("Digite outro número: ")),
     int(input("Digite mais um número: ")),
     int(input("Digite o penúltimo número: ")),
     int(input("Digite o último número: "))]
    
print(f'\nOs números digitados foram = \033[32m{n}\033[m')
print(f'O menor número foi o {min(n)}, nas posições: ', end=" ")
for i, c in enumerate(n):
    if c == min(n):
        print(i, end='... ')

print(f'\nO maior número foi o {max(n)}, nas posições: ', end=" ")
for i, c in enumerate(n):
    if c == max(n):
        print(i, end='... ')
