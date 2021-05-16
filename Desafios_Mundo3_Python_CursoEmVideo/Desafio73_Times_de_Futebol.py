# Programa com os times do brasileirão 2020 em ordem de colocação.
# Mostrar os 5 primeiros, os 4 últimos, em ordem alfabética, a posição
# de um time específico;
times = ("Flamengo", "Internacional", "Atlético Mineiro", "São Paulo", "Fluminense",
        "Grêmio", "Palmeiras", "Santos", "Athletico Paranaense", "Red Bull Bragantino",
        "Ceará", "Corinthians", "Atlético Goianiense", "Bahia", "Sport", "Fortaleza",
        "Vasco da Gama", "Goiás", "Coritiba", "Botafogo")
print("=" * 30)
print("{:^30}".format("TABELA BRASILEIRÃO 2020"))
print("=" * 30)

print("Times participantes do campeonato: ")
for i in sorted(list(times)):
    print(" ", i)

print("\nOs cinco primeiros colocados foram: ")
for i in range(5):
    print("{}-> {}".format(i+1, times[i]))

print("\nOs quatro últimos colocados foram: ")
for i in range(len(times)-4, len(times)):
    print("{}-> {}".format(i+1, times[i]))

while True:
    opcao = input("\nSaber a posição de um time: ")
    if opcao in times:
        print("\033[33mA posição do time é a {}\033[m".format(times.index(opcao)+1))
        break
    else:
        print("\033[31mVocê digitou incorretamente!\033[m")
