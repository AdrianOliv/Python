# Criar uma tupla com produtos e preços em seguida.
# Mostrar os valores através de informe tabular.

tupla = ()
for i in range(3):
    tupla += (input("Digite o produto: ").capitalize(), )
    tupla += (input("Digite o valor: ").capitalize(), )

for i in range(0, len(tupla), 2):
    print("{:^8} -> R$ {}".format(tupla[i], tupla[i+1]))

print("Programa Finalizado!")
