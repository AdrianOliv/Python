# Ler as notas de um aluno e decidir se aprovado, reprovado ou recuperacao.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5 :
    print(f'Sua média foi {media}. Você \033[31mREPROVOU!\033[m')
elif media > 7 :
    print(f'Sua média foi {media}. Você \033[32mPASSOU!\033[m')
else :
    print(f'Sua média foi {media}. Você está em \033[33mRECUPERACAO!\033[m')
