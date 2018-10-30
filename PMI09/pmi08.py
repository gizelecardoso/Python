#Informe as duas notas de um aluno (P1 e P2)
#e a quantidade de faltas no semestre,
#calcule a media das notas e o percentual de faltas
#sobre 20 aulas.  Caso o percentual de faltas
#for maior que 30% o aluno esta automaticamente reprovado,
#caso ao contrario verifique se a media e maior igual a 6,
#se afirmativo o aluno esta aprovado,
#senão informe uma nota P3 para recalcular a media,
#se a nova media for maior igual a 6,
#escreva aprovado no exame,
#caso negativo exiba reprovado por nota.

p1 = float(input("Informe a nota p1:"))
p2 = float(input("Informe a nota p2:"))
faltas = float(input("Quantidade de faltas:"))
percFaltas = faltas / 20
media = (p1+p2)/2
if percFaltas > 0.3 :
    print("Aluno reprovado por faltas")
else :
    if media >= 6 :
        print("Aluno aprovado :", media)
    else :
        p3 = float(input("Informe a nota p3 :"))
        media = (p1+p2+p3)/3
        if media >= 6:
            print("Aprovado no exame :", media)
        else :
            print("Reprovado no exame :", media)
            
            
