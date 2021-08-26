# Faça um programa que peça dois números, base e expoente,
# calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.

base = int(input("Insira o valor da base: "))
expoente = int(input("Insira o valor do expoente: "))
cont = 1
resultado = 1

while (cont <= expoente):
    resultado *= base
    cont += 1

print(f"{base} elevado à {expoente}ª potência é igual a {resultado}")