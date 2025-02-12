"""Escreva um programa que leia dois números e que pergunte qual operação
 você deseja realizar. Você deve poder calcular a soma (+), subtração (-),
   multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada."""

numero1 = int(input('Insira o numero 1: '))
numero2 = int(input('Insira o numero 2: '))
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
operacao = input('Escolha a operação \n soma (+) \n subtração (-) \n multiplicação (*) \n divisão (/) \n')

if operacao == '+':
    print('Resultado da operação: ', soma)

elif operacao == '-':
    print('Resultado da operação: ', subtracao)
    
elif operacao == '*':
    print('Resultado da operação: ', multiplicacao)
    
elif operacao == '/':
    print('Resultado da operação: ', divisao)

