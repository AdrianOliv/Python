# Ler um número de 0 a 9999 e mostrar na tela cada numero
# unidade, dezena, centena e milhar.
num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'''
    Unidade: {u}
    Dezena:  {d}
    Centena: {c}
    Milhar:  {m}\n''')
