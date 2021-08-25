# Bagin
def ficha(n="Desconhecido", g=0):
    return f'O jogador {n} fez {g} gol(s) na partida.'

# Main
nome = str(input("Nome do jogador: "))
gols = str(input("Gols marcados: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    print(ficha(g=gols))
else:
    print(ficha(nome, gols))
