#Peça ao usuário para informar a data de fabricação de um produto.
#Considere que ele vence em 180 dias.
#Mostre:
#A data de validade
#Se o produto ainda está válido ou já venceu
#Quantos dias faltam ou há quanto tempo passou do prazo

from datetime import datetime, timedelta

data_fabricacao = input('Digite a data de fabricação (formato: dd/mm/aaaa): ')

fabricacao = datetime.strptime(data_fabricacao, '%d/%m/%Y')

validade = fabricacao + timedelta(days=180)

hoje = datetime.now()

if validade > hoje:
    dias_restantes = (validade - hoje).days
    print(f'O produto ainda está válido. Data de validade: {validade.strftime("%d/%m/%Y")}. Faltam {dias_restantes} dias para o vencimento.')

elif validade < hoje:
    dias_passados = (hoje - validade).days
    print(f'O produto já venceu. Data de validade: {validade.strftime("%d/%m/%Y")}. Venceu há {dias_passados} dias.')

