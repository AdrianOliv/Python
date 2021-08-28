# Programa com palavras em uma tupla.
# Mostrar as vogais de cada palavra.

op = "y"
tupla = ()
while op == "y":
    tupla += (input("Uma Palavra: "), )
    while True:
        op = input("Continuar?(y/n) ")
        if op == "y" or op == "n":
            break
        else:
            print("Incorreto!")
            
print("{:.<11}{}".format("\nPalavra", "Vogais"))

for i in tupla:
    print("{:.<10}".format(i), end="")
    for j in "aeiou":
        if j in i:
            print(j, end=" ")
        if j == "u":
            print(" ")

# Outro jeito
for palavra in tupla:
    print("\nNa palavra '{}' temos as letras: ".format(palavra), end="")
    for letra in palavra:
    	if letra in "aeiou":
    		print(letra, end=" ")
    		
print("\n\nFim do Programa!")
