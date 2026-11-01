#Mostre quantos dias faltam para o dia 31 de dezembro do ano atual.

from datetime import datetime

agora = datetime.now()
ano_atual = agora.year
final_ano = datetime(ano_atual, 12, 31)

dias_restantes = (final_ano - agora).days

print(f'Faltam {dias_restantes} dias para o dia 31 de dezembro do ano {ano_atual}.')
