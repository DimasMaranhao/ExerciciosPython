# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []
contador = 1

for i in range(0,10):
    i = int(input("Digite o " + str(contador) + "º número: "))
    contador += 1
    lista.append(i)

print(lista)