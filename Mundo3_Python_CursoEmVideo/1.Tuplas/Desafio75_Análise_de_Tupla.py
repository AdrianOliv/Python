# Programa que lê 4 numeros do usuário.
# Depois analisa quantos "9" existem, posição do valor "3"
# E quais foram os números pares.

tupla = ()
for i in range(4):
    tupla = tupla + (int(input("Digite um valor: ")), )

# Quantas vezes aparece o numero 9.
print("\nO número nove apareceu {} vezes.".format(tupla.count(9)))

# A posição do valor 3.
if 3 in tupla:
    print("A posição do número três é a {}.".format(tupla.index(3)+1))
else:
    print("O número três não foi digitado!")

# Quais os números pares.
print("Números pares digitados: ", end='')
x = False
for i in tupla:
    if i % 2 == 0:
        print(" ", i, end="")
        x = True
    elif x == False and tupla.index(i) == (len(tupla)-1):
        print("Não houveram!")
