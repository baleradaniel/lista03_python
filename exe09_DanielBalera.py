"""Escreva um programa que faça o cálculo do imposto de renda 2025.
 Consulte a tabela no site da Receita federal."""

renda_mensal = float(input('Insira a renda mensal: '))

if renda_mensal <= 2259.20:
    aliquota = 'isento'
    print('Sua parcela mensal prevista: ', aliquota)
    print('Daniel Balera')

elif renda_mensal <= 2828.65:
    aliquota = renda_mensal*0.075
    print('Sua parcela mensal prevista: R$', aliquota)
    print('Daniel Balera')

elif renda_mensal <= 3751.05:
    aliquota = renda_mensal*0.15
    print('Sua parcela mensal prevista: R$', aliquota)
    print('Daniel Balera')

elif renda_mensal <= 4664.68:
    aliquota = renda_mensal*0.225
    print('Sua parcela mensal prevista: R$', aliquota)
    print('Daniel Balera')

else: 
    aliquota = renda_mensal*0.275
    print('Sua parcela mensal prevista: R$', aliquota)
    print('Daniel Balera')
    