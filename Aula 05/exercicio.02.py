#Exercício 02 - Trello

from random import shuffle

cor1 = str (input("Digite o nome de uma cor: "))
cor2 = str (input("Digite o nome de uma cor: "))
cor3= str (input("Digite o nome de uma cor: "))
cor4 = str (input("Digite o nome de uma cor: "))

cores = [cor1, cor2, cor3, cor4]

shuffle (cores) #embaralha

print(" "*5, "Cor Sorteada", " "*5) #polimorfismo
print (f"\n A cor sorteada foi: {cores}.") #Interpolação
































