# Programa para ler sete numeros.
# Adicionar em uma lista unica, separando pares e impares.

l = [[], []]
for i in range(7):
	num = int(input(f"Digite o {i+1} num: "))
	if num % 2 == 0:
		if num not in l[0]:
			l[0].append(num)
		else:
			if num not in l[1]:
				l[1].append(num)

print(f'\nOs números pares foram : {sorted(l[0])}')
print(f'Os números ímpares foram: {sorted(l[1])}')
