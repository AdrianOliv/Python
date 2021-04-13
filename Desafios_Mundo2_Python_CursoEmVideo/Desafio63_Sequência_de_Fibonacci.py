# Programa que lê um termo e mostra n valores
# da sequência de Fibonacci.
termos = int(input('Digitos a mostrar: '))
digit0 = i = 0
digit1 = final = 1
while i != termos:
    print('Termo {:>2}: {}'.format(i+1, final))
    final = digit1 + digit0
    digit0 = digit1
    digit1 = final
    i += 1
