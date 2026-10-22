pessoa = {
    'nome': 'Pedro',
    'idade': 17,
    'cidade': 'Rio de Janeiro',
    'profissoes': ['Engenheiro', 'Músico', 'Professor']
}

print(pessoa['nome'])  # Acessando o valor associado à chave 'nome'

print(pessoa['idade'])  # Acessando o valor associado à chave 'idade'

print(pessoa['cidade'])  # Acessando o valor associado à chave 'cidade'

pessoa['idade'] = 18  # Modificando o valor associado à chave 'idade'

del pessoa['cidade']  # Removendo a chave 'cidade' e seu valor associado

print(pessoa['profissoes'])  # Acessando o valor associado à chave 'profissoes'

print(pessoa.keys())  # Obtendo todas as chaves do dicionário

print(pessoa.values())  # Obtendo todos os valores do dicionário

print(list(pessoa.items()))  # Obtendo todos os pares de chaves e valores do dicionário

print(pessoa.items())  # Obtendo todos os pares de chaves e valores do dicionário


produtos = {
    'nome': 'Notebook',
    'preco': 3500.00,
    'estoque': 10
}

print(f'O produto {produtos["nome"]} custa R${produtos["preco"]:.2f} e possui {produtos["estoque"]} unidades em estoque.')



