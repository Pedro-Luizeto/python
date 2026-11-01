#Crie um programa que sorteia um número inteiro entre 1 e 10 usando a biblioteca random.
#O jogador tem que tentar adivinhar esse número.
#O jogo deve continuar perguntando até o jogador acertar.

#A cada tentativa, o programa deve informar:

#"Muito alto!" se o palpite for maior que o número sorteado

#"Muito baixo!" se for menor

#"Acertou!" se for igual

#Ao final, informe quantas tentativas foram necessárias para acertar.

from random import randint

numero_sorteado = randint(1, 10)
tentativas = 0

while True:
    palpite = int(input('Tente advinhar o número que foi sorteado entre 1 e 10: '))
    tentativas += 1

    if palpite == numero_sorteado:
        print('Parabéns você acertou !')
        print(f'Você precisou de {tentativas} tentativas para acertar.')
        break

    else:
        if palpite > numero_sorteado:
            print('Muito alto!')
        else:
            print('Muito baixo!')
        continue