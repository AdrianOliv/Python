# Digitar algo e mostrar todos os seus tipos primitivos.
algo = input('Digite algo: ')
print(f'O tipo primitivo é: {type(algo)}')
print(f'Tudo Maiúsculo: {algo.upper()}')
print(f'Tudo Minúsculo: {algo.lower()}')
print(f'Está Capitalizado: {algo.capitalize()}')
print(f'É Numérico: {algo.isnumeric()}')
print(f'É Alfabético: {algo.isalpha()}')
print(f'É Alfanumérico: {algo.isalnum()}')
print(f'É um digito: {algo.isdigit()}')
