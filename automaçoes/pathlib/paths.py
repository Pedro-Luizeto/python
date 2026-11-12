
from pathlib import Path

caminho = Path('arquivo.txt') # Caminho relativo para o arquivo 'arquivo.txt'

#caminho_absoluto = Path(r'C:\Users\Pedro Luizeto\Documents\arquivo2.txt') -> Caminho absoluto para o arquivo 'arquivo2.txt'

#caminho_absoluto = caminho.absolute() # Obtendo o caminho absoluto do arquivo 'arquivo.txt'


#print(caminho)
#print(caminho_absoluto)


# ------- PARTE 2 ---------
# Verificando se o arquivo existe e se é um arquivo ou diretório




#if caminho.exists():
    #print(f'O arquivo {caminho.name} existe.')
#else:
    #print(f'O arquivo {caminho.name} não existe.')


#if caminho.is_file():
    #print(f'O arquivo {caminho.name} é um arquivo.')

#elif caminho.is_dir():
    #print(f'O arquivo {caminho.name} é um diretório.')

#else:
    #print(f'O arquivo {caminho.name} não é um arquivo nem um diretório.')

nova_pasta = Path('nova_pasta')
#nova_pasta.mkdir() # Cria uma nova pasta chamada 'nova_pasta' no diretório atual
 
nova_pasta.mkdir(exist_ok=True, parents=True) # Cria a pasta 'nova_pasta' se ela não existir, caso contrário, não faz nada. O parâmetro 'parents=True' permite criar diretórios pai, se necessário.

arquivo = Path('arquivo.txt')
novapasta = Path(nova_pasta)

arquivo.unlink() # Remove o arquivo 'arquivo.txt' do diretório atual

nova_pasta.rmdir() # Remove a pasta 'nova_pasta' do diretório atual, desde que esteja vazia


arquivo = Path('arquivo.txt')
conteudo = arquivo.read_text(encoding='utf-8') # Lê o conteúdo do arquivo 'arquivo.txt' e armazena na variável 'conteudo'
arquivo.write_text('Novo conteúdo do arquivo.', encoding='utf-8') # Escreve o texto 'Novo conteúdo do arquivo.' no arquivo 'arquivo.txt', substituindo o conteúdo anterior

print(conteudo)

pasta = Path()
for arquivo in pasta.glob('*.txt'): # Itera sobre todos os arquivos com extensão '.txt' no diretório atual
    print(arquivo.name) # Imprime o nome de cada arquivo encontrado

print(caminho.stem) # Imprime o nome do arquivo sem a extensão

print(caminho.suffix) # Imprime a extensão do arquivo






 

