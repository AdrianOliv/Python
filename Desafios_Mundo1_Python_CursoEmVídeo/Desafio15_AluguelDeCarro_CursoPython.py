# Calcular aluguel de um carro.
dia = int(input('Por quantos dias o carro ficou alugado: '))
km = float(input('Qual a distância percorrida pelo carro: '))
print(f'O valor a ser pago é R$ {(60*dia)+(0.15*km)}.')
