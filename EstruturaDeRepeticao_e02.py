""" Faça um programa que leia um nome de usuário e a sua senha
e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro
e voltando  pedir as informações. """

user = input("Digite o nome do usuário: ")
password = input("Digite uma senha: ")

while (user == password):
    print ("\nA senha digitada é inválida!")
    user = input("Digite o nome do usuário: ")
    password = input("Digite uma senha: ")