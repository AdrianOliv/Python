# Desenvolva um programa em que o usuário insira um número.
# Seu programa deve imprimir a seqüência de Fibonacci para esse número ou para o enésimo número.

fibo = [1]

print("-" * 30)
print(f"\033[32m{'Sequência de Fibonacci':^30}\033[m")
print("=" * 30)

while True:
    n = int(input("Quantos digitos você quer mostrar: "))
    if n == 0:
        break
    while True:
        if n < 1:
            print("Incorreto")
            break
        elif len(fibo) < n:
            if len(fibo) == 1:
                fibo.append(1)
            else:
                fibo.append(fibo[len(fibo)-1] + fibo[len(fibo)-2])
        else:
            for i in range(n):
                print(fibo[i], end =" ")
            print("\n")
            break
