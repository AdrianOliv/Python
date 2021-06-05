# Programa para ler varios nomes e pesos.
# Mostrar total, maior peso e menor peso.

n = []
dado = []
i = mai = men = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
	
    if men == 0:
	men = dado[1]
    if dado[1] > mai:
	mai = dado[1]
    elif dado[1] < men:
	men = dado[1]
	
    n.append(dado[:])
    dado.clear()
    i += 1
    while True:
        op = input('Continuar(y/n)? ')
        if op in 'YyNn':
            break
        else:
            print('Valor incorreto.')
    if op in 'Nn':
	break

if len(n) == 1:
    print(f"\nFoi cadastrado somente uma pessoa e seu peso foi de {n[0][1]} kg.")
else:
    print(f'\nForam cadastrados {i} pessoas.')
    print(f'O maior peso foi {mai} kg do(s) participante(s):')
    for p in n:
	    if p[1] == mai:
	        print(p[0])
		
    print(f"O menor peso foi {men} kg do(s) participante(s):")
    for p in n:
        if p[1] == men:
	        print(p[0])
