#Usando loops, peça 5 números ao usuário (com input()), some todos e mostre o resultado.

soma = 0
for i in range(5):
    numero = int(input('Digite um número: '))
    soma += numero

print(f'A soma dos números digitados é: {soma}')

