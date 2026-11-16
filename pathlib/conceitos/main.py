#Fazer um programa que mostre o nome de todos os arquivos dentro da pasta Dados.

from pathlib import Path

# Caminho da pasta Dados
caminho = Path("Dados")

# Verifica se a pasta existe
if caminho.exists() and caminho.is_dir():
    # Lista todos os arquivos na pasta Dados
    arquivos = list(caminho.iterdir())
    
    # Verifica se há arquivos na pasta
    if arquivos:
        print("Arquivos na pasta Dados:")
        for arquivo in arquivos:
            if arquivo.is_file():
                print(arquivo.name)
    else:
        print("A pasta Dados está vazia.")