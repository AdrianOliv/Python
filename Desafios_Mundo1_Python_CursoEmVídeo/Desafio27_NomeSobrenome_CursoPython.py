# Ler o nome completo e mostrar na tela o primeiro e o ultimo.
nome = input('Digite seu nome completo: ').title().strip()
nome = nome.split()
print(f'Olá {nome[0]} {nome[len(nome)-1]}, tudo bem?')
