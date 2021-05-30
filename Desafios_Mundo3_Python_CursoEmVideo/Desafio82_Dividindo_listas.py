# Ler varios numeros do usuário e adicionar em uma lista.
# Criar uma lista de pares e impares a partir da primeira lista.

p = []
imp = []
l = []

while True:
	l.append(int(input("Digite um número: ")))

	while True:
		op = input("Continuar(y/n)? ")
		if op in 'yn':
			break
		else:
			print("Valor Inválido!")
	if op in "n":
		break

for i in l:
	if i % 2 == 0:
		p.append(i)
	else:
		imp.append(i)

print(f'\nVocê digitou os seguintes números {l}.')
print(f'Os números pares foram {p}.')
print(f'Os números ímpares são {imp}.')