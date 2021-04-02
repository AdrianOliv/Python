# Ler um nome completo e colocar em MAIÚSCULO, minúsculo, e
# quantas letras tem, sem considerar espaços e quantas letras tem o primeiro nome
nome = input('Digite seu nome completo: ').strip()
print(f'''
    Maiuscula: {nome.upper()}
    Minuscula: {nome.lower()}
    Total de letras: {len(nome.replace(" ",""))}
    Letras do primeiro nome: {len(nome.split()[0])}\n''')
