def leiaDin(x):
    """Valida se entrada de dados é númerico.

    Args:
        x ([str]): Texto inicial, como o Input

    Returns:
        [float]: Valor inserido formatado para float.
    """
    while True:
        print(x, end = '')
        num = input().strip().replace(',', '.')
        for i in range(len(num)):
            if num[i].isalpha() and num[i] != '.' or num.count('.') > 1 or num[i].isspace():
                break
            elif i == len(num)-1:
                return float(num)
        if num is float():
            break
        print('Você digitou um número incorreto!')