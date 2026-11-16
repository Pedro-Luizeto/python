from pathlib import Path
import shutil

# Caminho do arquivo
arquivo_vendas = Path("vendas.csv")

# Caminho da pasta de destino
pasta_dados = Path("Dados")

# Verifica se o arquivo existe
if arquivo_vendas.exists() and arquivo_vendas.is_file():

    # Verifica se a pasta existe
    if not pasta_dados.exists():
        pasta_dados.mkdir()
        print("Pasta Dados criada!")

    # Move o arquivo para a pasta
    shutil.move(
        str(arquivo_vendas),
        str(pasta_dados / arquivo_vendas.name)
    )

    print("Arquivo movido com sucesso!")

else:
    print("O arquivo vendas.csv não foi encontrado.")