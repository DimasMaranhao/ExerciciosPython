# Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = []
soma = 0
media = 0

for num in range (0,5):
    num = float(input("Insira um número: "))
    numeros.append(num)

soma = sum(numeros)
media = soma/5

print(f"\nA soma de todos os números inseridos é {soma}")
print(f"A média dos números inseridos é {media}")