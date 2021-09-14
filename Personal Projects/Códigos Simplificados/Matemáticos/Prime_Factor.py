# Programa de fatoração por números primos.

# Declarando variáveis.
lprime = list()
fact = list()
n = nn = 0

# Registrando números primos.
for i in range(1, 1001):
    for j in range(2, i + 1):
        if i % j == 0 and i != j:
            break
        else:
            lprime.append(i)
            break

# Programa
print("-" * 40)
print(f"\033[42m{'Prime fact':^40}\033[m")
print("=" * 40)

# If input error
try:
    n = int(input("Digite o N° que deseja fatorar: "))
    if n == 1:
        print("\n1 é fatorado por ele mesmo!")
    nn = n
    i = 2
    
    # Prime Fact
    while nn != 1:
        if nn < 1:
            print("\n\033[31mErro")
            print("Valores menores que 1 não são aceitos!\033[m")
            break
        elif lprime.index(i) == (len(lprime)-1):
            fact.clear()
            print("\n\033[31mERRO")
            print("Data base insuficiente para a fatoração!\033[m")
            break
        for i in lprime:
            if nn % i == 0:
                fact.append(i)
                nn = nn / i
                break
    
    if len(fact) != 0:
        print(f"\n\033[36mFatoração de {n} = \033[m", end = "")
        print(fact)

# Tratamento do Erro de Input
except:
    print("\n\033[31mValor digitado é inválido!\033[m")
