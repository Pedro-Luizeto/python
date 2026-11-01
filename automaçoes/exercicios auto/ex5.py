#Peça ao usuário que digite uma data de um evento

#Mostre se o evento já aconteceu, se está acontecendo hoje, ou quantos dias faltam.

from datetime import datetime

data_evento = input('Digite a data do evento(formato: dd/mm/aaaa):  ')

evento = datetime.strptime(data_evento, '%d/%m/%Y')

hoje = datetime.now()

if evento < hoje:
    print('O evento já aconteceu.')

elif evento > hoje:
    dias_restantes = (evento - hoje).days
    print(f'Faltam {dias_restantes} dias para o evento.')

elif evento.day == hoje.day and evento.month == hoje.month and evento.year == hoje.year:
    print('O evento está acontecendo hoje!')

