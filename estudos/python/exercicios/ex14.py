#Exercício 4 – Arrumando o texto
#Dada uma variável frase = "    @prendendo @ progr@m@r   "  com espaços nas pontas e letras bagunçadas, o programa deve:
#Trocar todas as letras "@" por "a"
#Remover espaços do início/fim
#Colocar a primeira letra de cada palavra em maiúsculo

frase = "    @prendendo @ progr@m@r   "

frase = frase.strip()

frase = frase.replace('@', 'a')

frase = frase.title()

print(f'A frase arrumada é: {frase}')