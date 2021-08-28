# Begin
def leiaInt(door):
    global cond
    cond = False
    print(door, end = ' ')
    num = input()
    if num.isnumeric():
        cond = True
    else:
        print('Valor Incorreto!')
        cond = False


# Main
while True:
    door = leiaInt("Escreva um número:")
    if cond:
        break
