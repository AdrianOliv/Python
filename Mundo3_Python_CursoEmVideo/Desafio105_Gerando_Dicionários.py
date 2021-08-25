# Begin
def notas(*a, Sit = False):
    """
    Função Notas\n
    Recebe várias notas do usuário e calcula o total de notas inseridas,
    o maior e menor valor, a média das notas e a situação escolar (opcional).

    Args:
        a (tuple): [uma tupla com os valores de nota inseridos]\n
        Sit (bool, optional): [Opcional de mostrar situação escolar]. Padrão: False.
    """
    boletim = dict()
    sum = float()
    boletim["Qtd de Notas:"] = len(a)
    boletim["Maior Nota:"] = max(a)
    boletim["Menor Nota:"] = min(a)
    for s in a:
        sum += s
    boletim["Média:"] = sum / len(a)
    if Sit:
        if boletim["Média:"] < 5:
            boletim["Sit:"] = "Ruim"
        elif boletim["Média:"] > 7:
            boletim["Sit:"] = "Ótimo"
        else:
            boletim["Sit:"] = "Regular"
    print(boletim)


# Main
notas(8,3,4,5,10)
print()
notas(7,2,5,6,10, Sit=True)