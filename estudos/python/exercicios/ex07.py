#Peça ao usuário uma nota de 0 a 10 para um filme. Classifique a avaliação assim:
#Nota 9 ou 10: "Excelente!"
#Nota 7 ou 8: "Muito bom"
#Nota 5 ou 6: "Regular"
#Menor que 5: "Ruim"

nota = float(input('Digite a nota do filme (0 a 10): '))


if nota >= 9 and nota <= 10:
    print('Excelente!')

elif nota >= 7 and nota < 9:
    print('Muito bom')

elif nota >= 5 and nota < 7:
    print('Regular')

elif nota < 5 and nota >= 0:
    print('Ruim')

else:
    print('Nota inválida! Digite uma nota entre 0 e 10.')