# Exercicio 04 - Trello

SalarioJunho = float(input("Digite o salário de junho: "))
SalarioJulho = float(input("Digite o salário de julho: "))
SalarioAgosto = float(input("Digite o salário de agosto: "))
SalarioSetembro = float(input("Digite o salário de setembro: "))

SomaSalarios = (SalarioJunho + SalarioJulho + SalarioAgosto + SalarioSetembro)

print("="*5, "Calculadora", "="*5) 
print(" O salário do mês de junho é: {:.2f}\n O salário do mês de julho é: {:.2f}\n O salário do mês de agosto é: {:.2f}\n O salário do mês de setembro é: {:.2f}\n"
.format (SalarioJunho, SalarioJulho, SalarioAgosto, SalarioSetembro))



