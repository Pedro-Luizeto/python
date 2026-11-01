#Crie uma função que receba como argumento um nome, e exiba uma assinatura desta forma:
#Assinatura gerada por [SEU NOME] em 24 de abril de 2025 às 15:02

def assinatura(nome):
    from datetime import datetime
    agora = datetime.now()
    data_formatada = agora.strftime("%d de %B de %Y às %H:%M")
    print(f"Assinatura gerada por {nome} em {data_formatada}")