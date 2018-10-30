mediaFinal = float(0)
mediaFaltas = float(0)
p1 = float(0)
p2 = float(0)
p3 = float(0)
faltas = int(0)

p1 = input("Digite a nota da prova 1: ")
p2 = input("Digite a nota da prova 2: ")
faltas = input("Digite a quantidade de faltas: ")

mediaFinal = (p1 + p2)/2
mediaFaltas = (faltas/20)*100

if mediaFaltas > 30:
    print("Aluno Reprovado por falta!")
elif mediaFinal >= 6:
    print("Aluno aprovado!")
elif mediaFinal < 6:
    p3 = input("Digite a nota da prova 3: ")
    mediaFinal = ((p1 + p2 + p3)/3)
    if mediaFinal >= 6:
        print("Aluno aprovado!")
    else:
         print("Aluno Reprovado por Nota!")
else:
     print("Aluno Reprovado por Nota!")

