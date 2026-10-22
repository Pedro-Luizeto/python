#Seu programa deve verificar se o usuário tem direito a frete grátis. As regras são:
#O valor da compra deve ser maior ou igual a 100
#E o cliente precisa estar cadastrado no programa de fidelidade
#Se as duas condições forem verdadeiras, mostre: "Frete grátis aplicado!"
#Caso contrário: "Frete não disponível gratuitamente."

valor_compra = float(input('Digite o valor da compra: '))

fidelidade = input('Você está cadastrado no programa de fidelidade? (sim/não): ').strip().lower()

if valor_compra >= 100 and fidelidade == 'sim':
    print('Frete grátis aplicado!')

else:
    print('Frete não disponível gratuitamente.')

