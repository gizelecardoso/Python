p1 = float(input("Digite a nota p1: "))
p2 = float(input("Digite a nota p2: "))
faltas = float(input("Quantidade de faltas: "))
percFaltas = (faltas/20)*100
media = (p1+p2)/2

if percFaltas < 0.3:
    print("Aluno reprovado por falta. ")
else:
    if media >=6:
        print("Aluno aprovado. ", media)
    else:
        p3 = float(input("Informe nota p3: "))
        mediaR = (p1+p2+p3)/3
        if mediaR >=6:
            print("Aluno aprovado no exame: ", mediaR)
        else:
            print("Aluno reprovado no exame: ", mediaR)
                       
