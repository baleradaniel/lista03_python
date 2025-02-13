"""Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
 Calcule o preço da passagem, cobrando R$ 0,50 por km para 
 viagens de até de 200 km, e R$ 0,45 para viagens mais longas."""

km = int(input('Qual a distancia? (km) '))

if km <= 200:
    cobrança = km*0.50
    print('Preço da viagem: ', cobrança)
    print('Daniel Balera')

else:
    cobrança = km*0.45
    print('Preço da viagem: ', cobrança)
    print('Daniel Balera')
