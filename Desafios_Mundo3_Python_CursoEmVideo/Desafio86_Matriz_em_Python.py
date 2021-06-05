# Programa que lê numeros e dispoe
# em uma matriz.

k = 1
m = [[], [], []]
for i in range(3):
    for j in range(3):
	m[i].append(int(input(f"Digite o {k} valor: ")))
	k += 1
		
for i in range(3):
    print("\n")
    for j in range(3):
	print(f'|{m[i][j]:^5}|', end = "")
