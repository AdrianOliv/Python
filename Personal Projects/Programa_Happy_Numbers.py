dados = list()
s = 0

dados.append(int(input("1° Termo: ")))
un = dados[-1]
i = False

while un != 1:
    print(dados)
    for n in str(un):
        s += int(n)**2
    if s in dados:
        print("\n\033[31mTermos Infinitos!\033[m")
        i = True
        break
    else:
        dados.append(s)
    s = 0
    un = dados[-1]

if un == 1:
    print("\n\033[32mHAPPY NUMBER!\033[m")
print(dados)
