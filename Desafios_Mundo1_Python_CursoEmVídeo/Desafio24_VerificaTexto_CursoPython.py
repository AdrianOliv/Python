# Ler o nome de uma cidade e dizer se começa com 'santo' ou 'santa'.
cidade = input('Digite o nome da cidade: ').strip().lower()
print(f'A cidade contem santo/santa: {cidade[:5]=="santo" or cidade[:5]=="santa"}')
