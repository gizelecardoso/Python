#Crie uma função em python que receba dois valores:
#Distancia em km, e consumo de Combustível de um carro,
#calcule quantos litros de combustível serão necessários
#para completar a viagem.

import math

def litros (d, c):
    l = d * c
    return l

       
consumo = litros(50, 10)
print("Quantos litros para concluir sua viagem de 50km: ", consumo , "litros")
            

#Crie uma função em python que dada uma distancia em km
#converta e exiba em milhas, onde 1Milha = 1,60934km

def quilometros (m):
    distancia = m /1.60934
    return distancia


distancia = quilometros(50)
print("A conversão de quilometros em milhas eh: ", distancia, "milhas" )
