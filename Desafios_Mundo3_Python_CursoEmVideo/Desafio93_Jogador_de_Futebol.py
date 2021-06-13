# Programa que lê nome do jogador, quantidade de partidas
# Gols por partida e mostra esse aproveitamento.
# No fim, guardar total de gols.

Jogador = {}
t = 0

Jogador['Nome'] = str(input("Nome do Jogador: "))
partidas = int(input("Jogos Realizados: "))
for p in range(partidas):
    Jogador[f'Partida{p+1}'] = int(input(f"Total Gols na Partida {p+1}: "))
    t += Jogador[f'Partida{p+1}']
Jogador['TotalGols'] = t
for i in Jogador.items():
    print(i)