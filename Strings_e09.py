# Verificação de CPF.
# Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
# e indique se é um número válido ou inválido através da validação dos dígitos verificadores
# e dos caracteres de formatação.

cpf = input("Digite seu CPF (xxx.xxx.xxx-xx): ").split(".")               #VALIDAÇÃO PELA SOMA DOS NUMEROS
cpf2 = cpf[0]
cpf3 = cpf[1]
cpf4 = cpf[2].split("-")
cpf5 = cpf4[0]
cpf6 = cpf4[1]
cpf_comp = cpf2+cpf3+cpf5+cpf6
numeros = []
numeros = list(map(int, cpf_comp))

if (sum(numeros) == 44):
    print("CPF VÁLIDO")
else:
    print("CPF INVÁLIDO")