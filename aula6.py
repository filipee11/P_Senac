'''
def fatorial  (a):
     if a == 0:
         return 1
     else:
        fat = 1 
        for i in range (1, a+1):
            fat *= 1
        return fat 

x = int(input("Digite um número inteiro:"))
print ("a fatorial de", x, "é" , fatorial)
'''
'''
nome= (input("Digite seu nome:"))
idade= int(input("Digite sua idade:"))
altura = float(input("Digite sua altura:"))
print (nome)
print (idade)
print("seu nome é: ",nome)
print("sua idade é: ",idade)
print("sua altura é: ",altura)
'''
def contagem_regressiva():
    numero = int(input("digite um número inteiro positivo: "))

    if numero <= 0:
        print("por favor, digite um número inteiro positivo.")
        contagem_regressiva()

    else: 
        while numero >= 0:
            print(numero)
            numero -= 1
contagem_regressiva()


def soma (a, b)
   return a + b 
def subtracao (a, b)
    return a - b
def multiplicacao (a, b)
    return a * b
def divisao (a, b)
    return a / b 