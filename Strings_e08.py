# Palíndromo.
# Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica
# se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos.
# Em textos mais complexos os espaços e pontuação são ignorados.
# A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
#
# Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

frase = input("Digite uma palavra ou frase (sem acentos ou caracteres especiais) para checarmos se a mesma é um palíndromo: ")
frase2 = frase.upper().replace(" ", "")
inverso = frase2[::-1]
palind = "não é um palíndromo"

if frase2 == inverso:
    palind = "é um palíndromo"

print(f"A frase digitada foi: {frase}")
print(f"A frase digitada {palind}")