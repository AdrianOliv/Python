# Programa Números Romanos
from time import sleep

# Funções
def Titulo():
    print("  +", "-" * 34, "+  ")
    print("  |", f'{"Números Romanos":^34}', "|  ")
    print("  +", "-" * 34, "+  ")
    print("  'Exit' para Sair!")

def Validar(word):
    global Numerais
    if "VV" in word or "LL" in word or "DD" in word:
        return False
    else:
        for letter in range(len(word)):
            if word[letter] not in Numerais.keys() or (word[letter] * 4) in word or word.count(word[letter]) > 4:
                return False
                break
            elif letter != len(word) - 1:
                if Numerais[word[letter]] < Numerais[word[letter+1]]:
                    if 0.1 > (Numerais[word[letter]] / Numerais[word[letter + 1]]) or (Numerais[word[letter]] / Numerais[word[letter + 1]]) > 0.2:
                        return False
                        break

def Romanos(word):
    global Numerais
    num = int()
    for letter in range(len(word)):
        if letter == len(word)-1:
            num += Numerais[word[letter]]
        elif Numerais[word[letter]] >= Numerais[word[letter+1]]:
            num += Numerais[word[letter]]
        else:
            if letter != 0:
                if word[letter] == word[letter - 1]:
                    return False
                    break
            num -= Numerais[word[letter]]
    if num != 0:
        return num

def Arabico(termo):
    global Numerais
    num = list()
    u = 1
    while termo != 0:
        for k, i in Numerais.items():
            if termo // i == u:
                if num.count(k) == 3:
                    if num[-1] == num[-2]:
                        for s in range(3):
                            num.pop()
                            termo += i
                        termo += i
                    else:
                        termo -= i
                    if len(num) > 0:
                        if num[-1] in "VLD":
                            if Numerais[num[-1]] == (5*i):
                                termo += Numerais[num[-1]]
                                num.pop()
                    num.append(k)
                    u = 0
                    break
                else:
                    num.append(k)
                    termo -= i
                    u = 0
                    break
        u += 1
    print("Romano: ", end = "")
    for h in num:
        print(h, end = "")
    print()


#Variables
Numerais = {"I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000}
termo = str()


#Program
Titulo()

while True:
    print()
    print("-" * 40)
    
    termo = str(input("Termo à descobrir: ").upper().strip())
    
    if termo == "EXIT" or termo == "SAIR":
        break
    elif termo == "":
        print("\033[33mNada foi digitado...\033[m")
    elif termo.isnumeric():
        print(Arabicos())
    elif termo.isalpha():
        if Validar(termo) == False:
            print("\033[31mErro Validação: Termo Inválido!\033[m")
        else:
            if Romanos(termo) == False:
                print("\033[31mErro Validação: termo inválido.\033[m")
            else:
                print(Romanos(termo))
    else:
        print("\033[31mErro: alfanumericos não permitidos.\033[m")
    
    sleep(0.5)
