# Programa que lê nome do jogador, quantidade de partidas
# Gols por partida e mostra esse aproveitamento.
# No fim, guardar total de gols.

jogadores = list()  # Lista Geral
jogador = dict()    # Dicionario Unico
gols = list()       # Gols de cada
partidas = mp = 0   # Num de Partidas e maior num
tgols = 0

while True:
    print('-' * 40)
    jogador['Nome'] = str(input("Nome do jogador: "))        # Nome do Jogador
    partidas = int(input("Jogos Realizados: "))              # Total Partidas
    if partidas > mp:
        mp = partidas
    for p in range(partidas):
        gols.append(int(input(f"Gols na Partida {p+1}: ")))  # Quantidade Gols por partida

    jogador['Gols'] = gols[:]                                # Adicionar gols na lista
    for i in gols:
        tgols += i
    jogador['TotalGols'] = tgols

    jogadores.append(jogador.copy())                         # Adicionar jogador na lista geral
    gols.clear()
    tgols = 0

    while True:                                              # Loop Recomeço
        o = input("Continuar(y/n): ")
        if o in 'YyNn':
            break
        else:
            print("\033[31mValor Incorreto!\033[m")
    if o in 'Nn':
        break

for j in jogadores:                  # Adiciona mesma quantidade de Partidas em todos os Jog.
    for i in range(mp - len(j['Gols'])):
        j['Gols'].append("-")

print('-' * 40)
print('\033[40mNome:     Total Gols:   Gols/Partidas:\033[m')
for i in jogadores:
    print(f'{i["Nome"]:<10}', end = "")
    print(f'{i["TotalGols"]:^11}', end = "   ")
    for j in i["Gols"]:
        print(f'{j:<3}', end = "")
    print()