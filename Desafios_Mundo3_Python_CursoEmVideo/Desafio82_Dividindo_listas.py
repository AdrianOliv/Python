# Ler varios numeros do usuário e adicionar em uma lista.
# Criar uma lista de pares e impares a partir da primeira lista.

p = []
imp = []
l = []

while True:
    l.append(int(input("Digite um número: ")))
	
    while True:
        op = input("Continuar(y/n)? ")
	    if op == "y" or op == "n":
	        break
	    else:
	        print("Valor inválido!")
        if op == "n":
            break

    for i in l:
        if i % 2 == 0:
            p.append(i)
        else:
            imp.append(i)

print(f'\nOs valores digitados foram: {l}')
print(f'Os valores pares: {p}')
print(f'E os ímpares: {imp}')
