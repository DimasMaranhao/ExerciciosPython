# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

nota1 = float(input("Insira a 1ª nota: "))
nota2 = float(input("Insira a 2ª nota: "))
nota3 = float(input("Insira a 3ª nota: "))
nota4 = float(input("Insira a 4ª nota: "))

media = (nota1+nota2+nota3+nota4)/4

print(f"1ª nota: {nota1}\n2ª nota: {nota2}\n3ª nota: {nota3}\n4ª nota: {nota4}\nMédia: {media}")