#Exercício 01 - Trello

import random

cor1 = str (input("Digite o nome de uma cor: "))
cor2 = str (input("Digite o nome de uma cor: "))
cor3= str (input("Digite o nome de uma cor: "))
cor4 = str (input("Digite o nome de uma cor: "))

cores = [cor1, cor2, cor3, cor4]

corEscolhida = random.choice(cores)

print(" "*5, "Cor escolhida", " "*5)
print (f"\n A cor escolhida foi: {corEscolhida}.") #Interpolação



















