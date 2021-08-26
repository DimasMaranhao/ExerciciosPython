# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Insira o nome: ")
aux = ""
while ((nome.count(aux)-1)<3):
    print(f"O nome inserido possui menos de três caracteres.")
    nome = input("Insira um nome válido: ")

idade = int(input("Insira a idade: "))
while ((idade <= 0) or (idade > 150)):
    print(f"Idade não válida!")
    nome = input("Insira uma idade válida: ")

salario = float(input("Insira o valor do salário: R$"))
while (salario <= 0):
    print("Salário não válido!")
    salario = float(input("Insira um valor de salário válido: R$"))

sexo = int(input("Insira o sexo:\n(1) para Masculino\n(2) para Feminino:  "))
while (sexo != 1) and (sexo != 2):
    print("Sexo não válido!")
    sexo = int(input("Insira o sexo:\n(1) para Masculino\n(2) para Feminino:  "))

est_civil = input("Insira o estado civil:\n(S) para Solteiro(a)\n(C) para Casado(a)\n(V) para Viúvo(a)\n(D) para Divorciado(a): ")
aux2 = est_civil.upper()
if aux2 == "C":
    situacao = "Casado(a)"
if aux2 == "S":
    situacao = "Solteiro(a)"
if aux2 == "V":
    situacao = "Viúvo(a)"
if aux2 == "D":
    situacao = "Divorciado(a)"

while aux2 not in ("S", "C", "V", "D"):
    print("Estado civil não válido!")
    est_civil = input("Insira o estado civil:\n(S) para Solteiro(a)\n(C) para Casado(a)\n(V) para Viúvo(a)\n(D) para Divorciado(a): ")


print(f"\n\nNome: {nome}\nIdade: {idade} anos\nSalário: R${salario}\nSexo: {sexo}\nEstado Civil: {situacao}")