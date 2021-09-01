from time import sleep

def aumentar(x, y = 10):
    """
    Aumenta o valor inserido com um percentual adicionado pelo usuário.

    Args:
        x ([float]): [valor inserido pelo usuário]
        y (int, optional): [percentual de aumento em %]. Defaults to 10.

    Returns:
        [float]: [retorna o valor inserido pelo usuário somado ao percentual de aumento]
    """
    y = y / 100
    return x * (1 + y)    


def diminuir(x, y = 10):
    """
    Diminui o valor inserido com um percentual adicionado pelo usuário.

    Args:
        x ([int/float]): [valor inserido pelo usuário]
        y (int, optional): [percentual de diminuição em %]. Defaults to 10.

    Returns:
        [int/float]: [retorna o valor inserido pelo usuário menos o percentual de diminuição]
    """
    y = y / 100
    return x * (1 - y)


def dobro(x):
    """
    Dobra o valor inserido pelo usuário.

    Args:
        x ([int/float]): [valor inserido pelo usuário]

    Returns:
        [int/float]: [x * 2]
    """
    return x * 2

def metade(x):
    """
    Divide o valor inserido pelo usuário em dois.

    Args:
        x ([int/float]): [valor inserido pelo usuário]

    Returns:
        [int/float]: [x / 2]
    """
    return x / 2

def moeda(x):
    """
    Formata o valor inserido como moeda brasileira - R$

    Args:
        x ([int/float]): [Valor à formatar]

    Returns:
        [int/float]: [R$ x]
    """
    return f'R$ {x}'

def resumo(x, y = 0, z = 0):
    """Resume os calculos dos exercícios anteriores em apenas uma função.

    Args:
        x ([int/float]): [Valor inserido pelo usuário]
        y (int, optional): [Valor de incrementação - %]. Defaults to 0.
        z (int, optional): [Valor de diminuição - %]. Defaults to 0.
    """
    print('\n========  CALCULO FINANCEIRO  ========')
    print(f'Preço Analisado: {moeda(x)}')
    print('{}% de Aumento: {}'.format(y, moeda(aumentar(x, y))))
    print('{}% de Diminuição: {}'.format(z, moeda(diminuir(x, z))))
    print('Dobro do Valor: {}'.format(moeda(dobro(x))))
    print('Metade do Valor: {}'.format(moeda(metade(x))))
    print('======== PROGRAMA FINALIZADO ========')
    sleep(3)