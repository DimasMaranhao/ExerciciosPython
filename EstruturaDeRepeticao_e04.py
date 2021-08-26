# Supondo que a população de um país A seja da ordem de 80000 habitantes
# com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes
# com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A
# ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

pop_a = 8000
taxa_a = 0.03
pop_b = 20000
taxa_b = 0.015
contador = 0


while (pop_a <= pop_b):
    pop_a += (pop_a * taxa_a)
    pop_b += (pop_b * taxa_b)
    contador += 1

print(f"Em {contador} anos, a população do País A será superior à população do País B.")


