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