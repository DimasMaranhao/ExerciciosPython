# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

n = int(input("Insira um número para conhecermos a sequencia de Fibonacci até o mesmo: "))
ultimo = 1
penultimo = 1
novo_num = 0
sequencia = [1,1]

if (n <= 1):
    print(sequencia)
else:
    for i in range (2, n):
        ultimo = sequencia[-1]
        novo_num = ultimo + penultimo
        ultimo = novo_num
        penultimo = (novo_num - penultimo)
        if (len(sequencia) <= n):
            sequencia.append(novo_num)

print(sequencia)