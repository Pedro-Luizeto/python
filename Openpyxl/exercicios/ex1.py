#Crie um arquivo chamado cadastro.xlsx com uma aba chamada Pessoas.
#Adicione os seguintes dados nas células manualmente (com planilha["A1"] = ...):

#| Nome     | Cidade         |
#|----------|----------------|
#| João     | Recife         |
#| Marina   | São Paulo      |
#| Otávio   | Belo Horizonte |

from openpyxl import Workbook

arquivo = Workbook()

planilha = arquivo.active
planilha.title = 'CADASTRO'

planilha['A1'] = 'Nome'
planilha['B1'] = 'Cidade'
planilha['A2'] = 'João'
planilha['B2'] = 'Recife'
planilha['A3'] = 'Marina'
planilha['B3'] = 'São Paulo'
planilha['A4'] = 'Otávio'
planilha['B4'] = 'Belo horizonte'




arquivo.save('cadastro.xlsx')


