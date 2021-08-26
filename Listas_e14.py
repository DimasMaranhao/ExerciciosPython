# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# As perguntas são:
#   * "Telefonou para a vítima?"
#   * "Esteve no local do crime?"
#   * "Mora perto da vítima?"
#   * "Devia para a vítima?"
#   * "Já trabalhou com a vítima?"
#   O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#   Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
#   entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

respostas = []

telef = int(input("O suspeito telefonou para a vítima?\n(1) SIM\t(2)NÃO : "))
respostas.append(telef)
local = int(input("O suspeito esteve no local do crime?\n(1) SIM\t(2)NÃO : "))
respostas.append(local)
moradia = int(input("O suspeito mora perto da vítima?\n(1) SIM\t(2)NÃO : "))
respostas.append(moradia)
divida = int(input("O suspeito devia algo para a vítima?\n(1) SIM\t(2)NÃO : "))
respostas.append(divida)
trab = int(input("O suspeito já trabalhou com a vítima?\n(1) SIM\t(2)NÃO : "))
respostas.append(trab)

analise = respostas.count(1)

if (analise>=2) and (analise < 3):
    print ("SUSPEITO")
elif (analise>=3) and (analise<5):
    print ("CÚMPLICE")
elif (analise == 5):
    print("ASSASSINO")
else:
    print("INOCENTE")
