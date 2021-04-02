# Programa que aprova empréstimo.
# Verificar Valor da Casa, Parcelas e Salário
# Negar empréstimo se parcela exceder 30% do salário.
print('-=' * 20)
print('{:^40}'.format("SIMULADOR DE EMPRESTIMO"))
print('-=' * 20)
emp = float(input('Qual o valor do empréstimo: '))
sal = float(input('Qual o valor do seu salário: '))
par = int(input('Quantas parcelas você deseja: '))
if (emp / par) < (0.30 * sal):
    print('\033[32mEmpréstimo Aprovado!')
    print('Serão {} parcelas de R$ {}!\033[m\n'.format(par, (emp / par)))
else:
    print('\033[31mEmprestimo Negado!\033[m\n')
