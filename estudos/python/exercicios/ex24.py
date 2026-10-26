#Crie um sistema de votação onde o usuário escolhe entre:
#1."Pizza"
#2."Hambrguer"
#3."Sair"
#Enquanto ele não digitar "3", continue perguntando
#No final, mostre quantos votos cada item recebeu

pizza = 0
hamburguer = 0
while True:
    print("Escolha uma opção:")
    print("1. Pizza")
    print("2. Hamburguer")
    print("3. Sair")
    escolha = input("Digite o número da sua escolha: ")

    if escolha == '1':
        pizza += 1
        print("Você votou em Pizza!")
    elif escolha == '2':
        hamburguer += 1
        print("Você votou em Hamburguer!")
    elif escolha == '3':
        break
    else:
        print("Opção inválida. Tente novamente.")