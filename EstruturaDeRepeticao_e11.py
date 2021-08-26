# Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
soma = 0
intervalo = []

for i in range (num1+1, num2):
    intervalo.append(i)
    print(i, end = " ")

soma = sum(intervalo)

print(f"\nA soma dos números entre {num1} e {num2} é {soma}")