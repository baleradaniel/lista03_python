"""Pergunte ao usuário se está chovendo e converta sua resposta em minúsculas para que não importe em que caso ele digite.
 Se ele responder "sim", pergunte se está ventando. Se ele responder "sim" a esta segunda pergunta, exiba a resposta "Está ventando muito para um guarda-chuva", caso contrário,
 exiba a mensagem "Pegue um guarda-chuva". Se ele não respondera sim à primeira pergunta, mostre a resposta "Aproveite o seu dia"."""

ischovendo = input('Está chovendo? ')

if ischovendo.__eq__('sim'):
    isventando =  input('Está ventando? ')

    if isventando.__eq__('sim'):
        print('Está ventando muito para um guarda-chuva')
    else:
        print('Pegue um guarda-chuva')
else:
    print('Aproveite o seu dia')