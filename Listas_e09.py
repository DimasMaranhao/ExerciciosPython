# Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.

import random           #A questão não pede para gerá-los aleatoriamente. Apenas para treinar.

A = []
quad = []

for i in range (0,10):
    num = random.randint(1, 1000)       #Gerará 10 números aleatórios entre 1 e 1000(para os números não ficarem muito extensos)
    A.append(num)
    quad.append(num**2)

print(f"Os dez números, gerados aletaoriamente entre 1 e 1000, foram: {str(A)[1:-1]}")
print(f"A soma dos quadrados dos números gerados é: {sum(quad)}")