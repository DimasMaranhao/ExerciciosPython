# Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor_a = [1,3,5,7,9,11,13,15,17,19]
vetor_b = [2,4,6,8,10,12,14,16,18,20]
vetor_c = []

for i in range(0, len(vetor_a)):
    vetor_c.append(vetor_a[i])
    vetor_c.append(vetor_b[i])

print(vetor_a)
print(vetor_b)
print(vetor_c)