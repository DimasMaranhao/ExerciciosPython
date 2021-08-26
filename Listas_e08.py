# Faça um Programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []
contador = 1

for i in range (0,5):
    age = int(input("Insira a idade da "+ str(contador) +"ª pessoa: "))
    idades.append(age)
    height = float(input("Insira a altura da "+ str(contador) +"ª pessoa: "))
    alturas.append(height)
    contador += 1

alt_rev = sorted(alturas, reverse = True)
id_rev = sorted(idades, reverse = True)

print(f"Lendo as idades na ordem em que foram inseridas, temos: {str(idades)[1:-1]}")
print(f"Lendo as alturas na ordem em que foram inseridas, temos: {str(alturas)[1:-1]}")
print(f"Lendo as idades na ordem inversa, temos: {str(alt_rev)[1:-1]}")
print(f"Lendo as idades na ordem inversa, temos: {str(id_rev)[1:-1]}")