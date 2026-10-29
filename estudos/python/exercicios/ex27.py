#Crie uma função chamada verificar_par(numero) que retorna:
#"Par" se o número for par
#"Ímpar" se for ímpar
#Peça um número ao usuário com input(), chame a função e mostre o resultado.

def verificar_par(numero):
    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")


numero = int(input("Digite um número: "))
verificar_par(numero)