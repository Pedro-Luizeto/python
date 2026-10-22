frutas = ['Maçã', 'Banana', 'Laranja']

print(frutas[1])  # Acessando o segundo elemento da lista (índice 1)

print(frutas[-1])  # Acessando o último elemento da lista (índice -1)

frutas.append('Melancia')  # Adicionando um elemento ao final da lista

frutas[2] = 'Uva' # Modificando o terceiro elemento da lista (índice 2)

print(len(frutas))  # Obtendo o tamanho da lista

frutas.insert(1, 'Abacaxi')  # Inserindo um elemento na posição 1

frutas.sort()  # Ordenando a lista em ordem alfabética

frutas.clear()  # Limpando todos os elementos da lista

print(frutas.index('Banana'))  # Obtendo o índice do elemento 'Banana'

print(frutas.count('Laranja'))  # Contando quantas vezes 'Laranja' aparece na lista

frutas2 = frutas.copy()  # Criando uma cópia da lista frutas

frutas2.append('Pera')  # Adicionando 'Pera' à lista frutas2
frutas2.append('Manga')  # Adicionando 'Manga' à lista frutas2

print(frutas)  # Imprimindo a lista frutas
print(frutas2)  # Imprimindo a lista frutas2