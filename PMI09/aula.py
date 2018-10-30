import math

def multiplica(x, y):
    r = x * y
    return r

def qualSeuNome(p):
    print("Seu nome = ", p)


print("fatorial = ", math.factorial(6))
print("trunc = ", math.trunc(5.5436))#remove a parte decimal
print("arredondar = ", math.floor(6.3223))#arredonda para baixo

print("PI = ", math.pi)

print("Raiz quadrada = ", math.sqrt(25))

print("Potência = ", math.pow(6, 3))# 6 elevado a 3

# lista de funções de string

s = "lista de funções de string"
print("Conta a quantidade de caracteres: ", len(s))
print("Pegar a 3 letra:", s[3])
print("Pegar um substring: ", s[0:5])

lista = s.split(" ")#qual caracter para quebrar o texto, tranforma em um vetor de palavras
print(lista)

s = s.replace("lista" , "Conjunto")
print(s)

print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())

t = "Aulas de python"
print(t.ljust(50))#de uma espaço de 50 posições
print(t.center(50))
print(t.rjust(50))

print(t.ljust(50,"*"))#de uma espaço de 50 posições
print(t.center(50,"="))
print(t.rjust(50,"+"))


#import biblioteca de data

from datetime import date

data = date.today()
print(data)


print(multiplica(34,65))
print(qualSeuNome("Maria"))


