#Exercício 2 – Pegando um trecho da frase
#Peça ao usuário uma frase e dois números: início e fim. Mostre o fatiamento da frase entre esses índices.

frase = input('Digite uma frase: ')
inicio = int(input('Digite o índice inicial: '))
fim = int(input('Digite o índice final: '))

print(f'O trecho da frase é: {frase[inicio:fim]}')
