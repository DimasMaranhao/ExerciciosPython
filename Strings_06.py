# Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa)
# do usuário e imprima a data com o nome do mês por extenso.
#
# Data de Nascimento: 29/10/1973
# Você nasceu em  29 de Outubro de 1973.



data = input("Digite a data de seu nascimento (dd/mm/aaaa): ").split("/")
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])
contador = 0

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for i in range (1, mes):
    contador += 1
    mes = meses[contador]

print(f"Você nasceu em {dia} de {mes} de {ano}.")