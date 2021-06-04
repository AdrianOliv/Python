# Criar programa para validar uma expressão.
# Na verdade, ele valida se a sequencia de "()"
# está correta.

l = []
exp = str(input("Digite a expressão: "))

for i in exp:
    if i == "(":
        l.append("(")
    elif i == ")":
        if len(l) > 0:
            l.pop()
        else:
            l.append(')')

if len(l) == 0:
    print('\033[32mSua expressão é válida!\033[m')
else:
    print('\033[31mSua expressão NÃO é válida!\033[m')