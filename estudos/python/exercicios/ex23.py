#Peça ao usuário que vá digitando valores para guardar no cofrinho (em reais).
#Quando o usuário digitar 0, o programa para e mostra o total economizado.

total = 0
while True:
    valor = float(input('Digite um valor para guardar no cofrinho (ou 0 para sair): '))
    if valor == 0:
        break
    total += valor

print(f'Total economizado: R${total:.2f}')

