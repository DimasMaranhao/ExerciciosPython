# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

meses = []
temperaturas = []
meses_acima = []
temp_acima = []

for i in range (0,3):
    mes = input("Insira o mês: ")
    meses.append(mes)
    temp = float(input("Insira a temperatura de "+ str(mes)+":"))
    temperaturas.append(temp)

media = (sum(temperaturas)/len(temperaturas))

for x, y in zip (temperaturas, meses):
    if (x>media):
        temp_acima.append(x)
        meses_acima.append(y)

print(f"Média anual: {round(media, 1)}")
print(f"\n\nMESES COM TEMP\nACIMA DA MÉDIA\t\t\tTEMPERATURAS")
print("====================================")
for a, b in zip (meses_acima, temp_acima):
    print(a, "\t\t\t\t ", b,"ºC")