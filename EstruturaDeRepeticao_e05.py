# Altere o programa anterior permitindo ao usuário informar as populações e as taxas
# de crescimento iniciais. Valide a entrada e permita repetir a operação.

pop_a = 0
taxa_a = 0
tx_real_a = 0
pop_b = 0
taxa_b = 0
tx_real_b = taxa_b/100
contador = 0

while (pop_a < 1):
    pop_a = float(input("Digite o número de habitantes do País A: "))
    taxa_a = float(input("Digite a taxa de crescimento do País A (em %): "))
    tx_real_a = taxa_a/100

while (pop_b < 1):
    pop_b = float(input("Digite o número de habitantes do País B: "))
    taxa_b = float(input("Digite a taxa de crescimento do País B (em %): "))
    tx_real_b = taxa_b/100

while (pop_a <= pop_b):
    pop_a += (pop_a * tx_real_a)
    pop_b += (pop_b * tx_real_b)
    contador += 1

print(f"\nEm {contador} anos, a população do País A será superior à população do País B.\nPopulação do País A: {round(pop_a,1)} habitantes.\nPopulação do País B: {round(pop_b,1)} habitantes.")