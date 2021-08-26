# Faça um programa que leia 5 números e informe o maior número.

numeros = []
for num in range (0, 5):
    num = int(input("Insira um número inteiro: "))
    numeros.append(num)

print(f"\nO maior número inserido foi {max(numeros)}")