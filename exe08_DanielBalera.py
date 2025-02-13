"""Escreva um programa que pergunte a velocidade do carro de um usuário.
 Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
 Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h."""

velocidade = int(input('Insira a velocidade: '))
excesso_de_velocidade = 80

if velocidade > excesso_de_velocidade:
    multa = float((velocidade - excesso_de_velocidade)*5)
    print('Com o excesso de velocidade ultrapasado, você será multado no valor de R$', multa)
    print('Daniel Balera')
