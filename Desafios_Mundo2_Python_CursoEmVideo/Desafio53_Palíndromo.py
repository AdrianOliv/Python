# Programa detectar palíndromo.
# adicionando o lower no fim da frase ele reconhecerá
# mesmo se a frase estiver capitalizada.
frase = input('Digite algo: ').lower()
frase_contra = frase[::-1]
if frase_contra == frase:
    print('\033[32mÉ um palíndromo!\033[m')
else:
    print('\033[31mNão é um palíndromo!\033[m')
