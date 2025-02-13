"""Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
 Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%."""

salario =  float(input('Informe o seu salário: '))

if salario > 1250:
    aumento = salario* 0.10
    print('Salario atual: R$',salario, '\n Aumento: R$', aumento, '\n Salario pós aumento: R$', (salario + aumento))
    print('Daniel Balera')

else:
    aumento = salario* 0.15
    print('Salario atual: R$',salario, '\n Aumento: R$', aumento, '\n Salario pós aumento: R$', (salario + aumento))
    print('Daniel Balera')
