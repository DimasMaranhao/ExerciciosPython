# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário
# (incluindo espaços em branco), conte:
#
# a. quantos espaços em branco existem na frase.
# b. quantas vezes aparecem as vogais a, e, i, o, u.

frase = input("Digite uma frase: ").lower()

brancos = frase.count(" ")
vogal_a = frase.count("a")
vogal_e = frase.count("e")
vogal_i = frase.count("i")
vogal_o = frase.count("o")
vogal_u = frase.count("u")
total_vogais = 0

for i in frase:
    if (i == "a") or (i == "e") or (i == "i") or (i == "o") or (i == "u"):
        total_vogais += 1


print (f"Existem {brancos} espaço(s) em branco na frase.")
print(f"Existem {total_vogais} vogais na frase:\nA: {vogal_a}\nE: {vogal_e}\nI: {vogal_i}\nO: {vogal_o}\nU: {vogal_u}")