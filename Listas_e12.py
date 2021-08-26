# Foram anotadas as idades e alturas de 5 alunos.
# Faça um Programa que determine quantos alunos com mais de 13 anos
# possuem altura inferior à média de altura desses alunos.

alunos =[]
idades = []
alturas = []
nomes_validos = []
mais_velhos = []
mais_baixos = []
# media_alt = []

for i in range (0,3):
    nome = input("Insira o nome do(a) aluno(a): ")
    alunos.append(nome)
    age = int(input("Insira a idade do(a) aluno(a): "))
    idades.append(age)
    height = float(input("Insira a altura do(a) aluno(a): "))
    alturas.append(height)

media = (round((sum(alturas))/len(alturas),2))
# media_alt.append(media)

for x, y, z in zip (alunos, idades, alturas): # -------------> ESTRUTURA PARA LOOP FOR EM VARIAS LISTAS!!!
    if (y >= 13) and (z < media):
        nomes_validos.append(x)
        mais_velhos.append(y)
        mais_baixos.append(z)

print(f"\n\nAltura Média: {media}\n{len(mais_baixos)} alunos possuem idade superior a 13 anos e altura abaixo da média:")
print(f"\n\tALUNO(A):\t\t\t\tIDADE:\t\t\t\tALTURA:")
print("============================================================")
for n, o, p in zip (nomes_validos, mais_velhos, mais_baixos):
    print("\t",n,"\t\t\t\t",o,"\t\t\t\t",p)