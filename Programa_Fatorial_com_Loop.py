def fat(num):
    if num == 0:
        return 1
    elif num == 1:
        return num
    else:
        return num * fat(num-1)

try:
    x = 1
    while x > 0:
        x = int(input('Num: '))
        print(fat(x))
except:
    print('Você finalizou!')
