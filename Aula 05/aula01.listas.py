#Listas

import random

n1 = str (input("Digite um nome: "))
n2 = str (input("Digite um nome: "))
n3 = str (input("Digite um nome: "))
n4 = str (input("Digite um nome: "))

lista = [n1, n2, n3, n4]

sorteado = random.choice(lista) #choice

print("O nome Sorteado foi {}!".format(sorteado)) # {}máscara de substituição!






