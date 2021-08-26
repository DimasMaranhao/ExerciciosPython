# Número por extenso.
# Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

num = int(input("Digite um número entre 1 e 99: "))

while (num < 1) or (num > 99):
    num = int(input("Tente novamente! Digite um número entre 1 e 99: "))

aux = str(num)
temp = list(aux)
dezena = ""
unidade = ""

unidades_num = [1,2,3,4,5,6,7,8,9]
unidades = ["um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]

dezenas_num = [10,20,30,40,50,60,70,80,90]
dezenas = ["dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

especiais_num = [11,12,13,14,15,16,17,18,19]
especiais = ["onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

#11 a 19:
for (x, y) in zip (especiais_num, especiais):
    if x == num:
        print(y)

#Dezenas Fechadas:
for (x, y) in zip (dezenas_num, dezenas):
    if x == num:
        print(y)

#Demais Números:
if ((num>=1) and (num<10)) or ((num>=21) and (num<30)) or ((num>=31) and (num<40)) or ((num>=41) and (num<50)) or ((num>=51) and (num<60)) or ((num>=61) and (num<70)) or ((num >= 71) and (num < 80)) or ((num >= 81) and (num < 90)) or ((num >= 91) and (num < 100)):
    for (k, w) in zip (unidades_num, dezenas):
        if k == int(temp[0]):
            dezena = w
    for (m, n) in zip (unidades_num, unidades):
        if m == int(temp[1]):
            unidade = n
    print(f"{dezena} e {unidade}")