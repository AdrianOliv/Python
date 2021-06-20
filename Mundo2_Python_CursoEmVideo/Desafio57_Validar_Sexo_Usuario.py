# Programa para ler o sexo na forma 'F' e 'M', senão repeticao até acertar.
i = False
while i == False:
    s = input('Qual o seu sexo?(F/M) ')
    if s == 'M' or s == 'F' :
        i = True
    else:
        print('Você digitou incorretamente.')
print('FIM!')
