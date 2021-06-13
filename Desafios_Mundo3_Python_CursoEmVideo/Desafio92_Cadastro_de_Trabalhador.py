# Programa que lê nome, ano de nasc. e carteira de trabalho,
# adicionando idade em um dicionario
# Se o CTPS(Carteira de Trabalho) for diferente de zero,
# o dicionario recebera Ano de contrataçao e salário.
# Calcule e acrescente além da idade, com quantos anos a pessoa
# vai se aposentar.

from datetime import datetime
trab = {'Nome':'', 'Idade':'', 'CTPS':''}
trab['Nome'] = str(input("Nome da pessoa: "))
trab['Idade'] = datetime.today().year - int(input("Ano de Nasc: "))
trab['CTPS'] = int(input("Nº da CTPS: "))
if trab['CTPS'] != 0:
    trab['AContrat'] = int(input("Ano de contratação: "))
    trab['Salário'] = float(input("Salário: R$ "))
trab['Aposentadoria'] = 65 - trab['Idade']

print()
for i in trab.items():
    print(i)