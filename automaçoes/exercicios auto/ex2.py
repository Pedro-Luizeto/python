#Crie um programa que exiba quantos meses faltam para o ano acabar. Exemplo:

#Hoje é o 4º mês do ano. Ainda faltam 8 meses para terminar o ano!

from datetime import datetime

agora = datetime.now()
print(f'Hoje é {agora.month}º mês do ano. Ainda faltam {12 - agora.month} meses para terminar o ano!')

