#Crie uma função chamada apresentar_pessoa(nome, idade) que exibe a seguinte mensagem:

#"Nome: <nome> | Idade: <idade> anos"

def apresentar_pessoa(nome, idade):
    nome = str(input("Digite seu nome: "))
    idade = int(input('Digite sua idade: '))

    print(f"Nome: {nome} | Idade: {idade} anos")

apresentar_pessoa()