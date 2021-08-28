# Begin
from datetime import date

def voto(ano):
    if date.today().year - ano < 16:
        return "NEGADO"
    elif date.today().year - ano > 17 or date.today().year - ano > 65:
        return "OBRIGATÓRIO"
    else:
        return "OPCIONAL"


# Main
ano = int(input("Digite o seu ano de nascimento: "))
print(f"Devido a sua idade, voto {voto(ano)}")
