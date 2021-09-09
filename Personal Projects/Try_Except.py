# Usando Try e Except
# A função try é excelente para evitar erros de programa,
# principalmente quando o usuário erra o tipo de entrada.

try:
    #Erro proposital, causado por uma string em uma função de inteiro.
    print(int('Texto'))
except:
    # Se aparecer algum problema
    print('\nValor Inválido')
finally:
    print('Aparece no fim do programa, seja depois do try ou except!\n')