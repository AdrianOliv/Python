# Um programa que escreve o número do usuário por extenso.
# Somente números de 0 a 20;
numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete",
            "oito", "nove", "dez", "onze", "doze", "treze", "quatorze",
            "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
num = 99
while num < 0 or num > 20:
    num = int(input("Digite um número entre 0 e 20: "))
    if num < 0 or num > 20:
        print("\033[31mOpção Incorreta! Digite novamente.\033[m")
    else:
        print("Você digitou o número {}".format(numeros[num].capitalize()))

print("\033[32mPROGRAMA ENCERRADO!\033[m")