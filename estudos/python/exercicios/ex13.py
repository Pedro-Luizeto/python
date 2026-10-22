#Exercício 3 – Detectando palavras proibidas
#Peça ao usuário para escrever uma mensagem. Verifique se ela contém a palavra "bomba", e imprima um alerta se sim.

mensagem = input('Digite uma mensagem: ')

if 'bomba' in mensagem.lower():
    print('Alerta: A mensagem contém a palavra proibida "bomba".')

else:
    print('A mensagem não contém palavras proibidas.')