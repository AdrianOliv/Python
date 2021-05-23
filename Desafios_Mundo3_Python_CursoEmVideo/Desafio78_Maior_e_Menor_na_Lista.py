# Programa que lê 5 valores em lista.
# Mostrar o maior e o menor.

n = [int(input("Digite um número: ")),
     int(input("Digite outro número: ")),
     int(input("Digite mais um número: ")),
     int(input("Digite o penúltimo número: ")),
     int(input("Digite o último número: "))]
    
print(f'\nOs números digitados foram = \033[32m{n}\033[m')
print(f'O maior número foi \033[32m{max(n)}\033[m.')
print(f'O menor número foi \033[32m{min(n)}\033[m.')
