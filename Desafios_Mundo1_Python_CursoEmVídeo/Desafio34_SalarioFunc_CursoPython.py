# Ler salário e aumentar se: >1250 então 10%
# <=1250 então 15%
sal = float(input('Digite o seu salário: '))
if sal > 1250 :
    print(f'Seu nome salário é de R$ {sal * 1.1:.2f}!\n')
else:
    print(f'Seu novo salário é de R$ {sal * 1.15:.2f}!\n')
