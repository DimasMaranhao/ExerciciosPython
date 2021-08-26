# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas
# seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento
# e são iguais ou diferentes no conteúdo.
#
# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.

str1 = "Brasil Hexa 2006"
str2 = "Brasil! Hexa 2006!"
# str2 = "Brasil Hexa 2006"
tamanhos = ""
conteudo = ""

if ((len(str1)) > (len(str2))) or ((len(str1)) < (len(str2))):
    tamanhos = "tamanhos diferentes"
else:
    tamanhos = "tamanhos iguais"
for (x, y) in zip (str1, str2):
    if x != y:
        conteudo = "conteúdo diferente"
    if x == y:
        conteudo = "conteúdo igual"

print(f"Tamanho de \"Brasil Hexa 2006\": {len(str1)} caracteres")
print(f"Tamanho de \"Brasil! Hexa 2006!\": {len(str2)} caracteres")
print(f"As duas strings são de {tamanhos}.")
print(f"As duas strings possuem {conteudo}.")