# Programa que altera valor
# conforme pagamento

print('#' * 30)
print(f"{'FINALIZAÇÃO DE PAGAMENTO':^30}")
print('#' * 30)

v = int(input("Qual o valor?  "))

print('''\n1- Dinheiro (-5%)
2- Cartão Débito
3- Cartão Crédito (+5%)''')
o = int(input("Qual a forma de pagamento?   "))

if o == 1:
    print(f"\nValor Total: R$ {v*0.95:1.2f}")
elif o == 2:
    print(f"\nValor Total: R$ {v}")
elif o == 3:
    print(f"\nValor Total: R$ {v*1.05:1.2f}")
else:
    print("\033[31mForma de Pagamento Incorreto!\033[m")
