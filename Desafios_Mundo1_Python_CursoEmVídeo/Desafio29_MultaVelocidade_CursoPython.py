# Ler velocidade do carro, se maior que 80KM/h, multa de R$7/km acima
vel = float(input('Qual a velocidade do veículo: '))
if vel > 80:
    print('Você está acima do permitido e será multado.')
    print(f'A multa será de R${(vel-80)*7}!')
else:
    print('Velocidade dentro da permitida!')
