# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números
# pares e a quantidade de números impares.

pares = []
impares = []
for i in range (0,10):
    i = int(input("Digite um número: "))
    if (i%2 == 0):
        pares.append(i)
    else:
        impares.append(i)

print(f"\nNúmeros pares: {len(pares)}")
print(f"Números ímpares: {len(impares)}")