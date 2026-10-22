#Crie um sistema de login com dois dicionários: um que guarda as credenciais corretas, e outro dicionário que guarde as informações inseridas pelo usuário. Peça ao usuário para digitar o usuário e senha, e verifique se está correto de acordo com o primeiro dicionário.

#Se o usuário e a senha estão corretos → "Login bem-sucedido"

#Senão → "Usuário ou senha incorretos"

credenciais_corretas = {
    'usuario': 'adimin',
    'senha': '1234'
}

informacoes_usuario = {}

informacoes_usuario['usuario'] = input('Digite seu usuário: ')

informacoes_usuario['senha'] = input('Digite sua senha: ')

if informacoes_usuario['usuario'] == credenciais_corretas['usuario'] and informacoes_usuario['senha'] == credenciais_corretas['senha']:
    print('Login bem-sucedido')

else:
    print('Usuário ou senha incorretos')