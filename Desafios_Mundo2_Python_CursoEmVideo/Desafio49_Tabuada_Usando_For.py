# Criar uma tabuada usando o laço de repetição
n = int(input('Digite um número: '))
for i in range(1, 11):
    print('{:2}  * {:2} = {:3}'.format(n, i, n*i))
print('FIM!')
