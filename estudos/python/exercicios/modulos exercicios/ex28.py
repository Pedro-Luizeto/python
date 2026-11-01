#Importe as funções dos dois arquivos

#Peça ao usuário um número e mostre o dobro e a metade

#Dê boas-vindas usando o nome digitado

nome = input("Digite seu nome: ")
boas_vindas(nome)

from mensagens import boas_vindas
from matematica import dobro, metade

numero = float(input("Digite um número: "))
print(f"O dobro de {numero} é {dobro(numero)}")
print(f"A metade de {numero} é {metade(numero)}")

boas_vindas(nome)
