"""Peça ao usuário para inserir 1, 2 ou 3. Se ele inserir um 1, exiba a mensagem "Obrigado",
 se ele inserir um 2, exiba "Muito bem", se ele inserir um 3, exiba "Correto".
 Se ele inserir qualquer outra coisa, exiba "Mensagem de erro"."""

numero = int(input('Insira 1,2 ou 3: '))

if numero == 1:
    print('Obrigado')
elif numero == 2:
    print('Muito bem')
elif numero == 3:
    print('Correto')
else:
    print('Mensagem de erro')