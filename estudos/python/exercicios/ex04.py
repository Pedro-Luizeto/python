#Verificador de Nota Mínima: Crie um código que pergunte ao usuário qual foi sua nota em um teste. Defina uma nota mínima para aprovação (por exemplo, 6). Use uma estrutura if para verificar se a nota do usuário é maior ou igual à nota mínima. Se for, exiba a mensagem "Você atingiu a nota mínima!".

nota = float(input("digite sua nota: "))

if nota >= 6:
    print('Você atingiu a nota mínima!')
else:
    print('Você não atingiu a nota mínima.')

