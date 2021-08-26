# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

list = []
contador = 0

for i in range (0,5):
    i = int(input("Digite um número: "))
    list.append(i)
    contador += 1

print(f"\n{list}")