# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

import random

numeros = []
pares = []
impares= []

for i in range (1, 21):
    i = (random.randint(1, 21))
    numeros.append(i)

for x in numeros:
    if x%2 == 0:
        pares.append(x)
    else:
        impares.append(x)

numeros_ord = sorted(numeros)
pares_ord = sorted(pares)
impares_ord = sorted(impares)
print(f"Números aleatórios iniciais: {numeros_ord}\nPares: {pares_ord}\nÍmpares: {impares_ord}")