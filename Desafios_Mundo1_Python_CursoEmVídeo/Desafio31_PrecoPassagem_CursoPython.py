# Leia a distância e calcule a passagem cobrando:
# R$0,50/km até 200km e R$0,45/km acima de 200km
dist = float(input('Qual a distância da sua viagem? '))
if dist <= 200 :
    print(f'O valor da passagem é R$ {dist * 0.5}.\n')
else:
    print(f'O valor da passagem é R$ {dist * 0.45}.\n')
