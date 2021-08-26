# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

from math import prod

numeros = []

for i in range (0, 5):
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)

soma = sum(numeros)
multip = prod(numeros)

print(f"\nOs números inseridos foram: {str(numeros)[1:-1]}")
print(f"A soma de todos os números inseridos é: {soma}")
print(f"A multiplicação de todos os números inseridos é: {multip}")