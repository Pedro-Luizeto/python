#Mostre a hora atual no terminal, mas com a seguinte regra:

#Se a hora for antes das 12h, imprima: "Bom dia!"

#Se estiver entre 12h e 18h: "Boa tarde!"

#Depois disso: "Boa noite!

from datetime import datetime

agora = datetime.now()

print(f'Agora são {agora}')

if agora.hour < 12:
    print('Bom dia!')

elif 12 <= agora.hour < 18:
    print('Boa tarde!')

else:
    print('Boa noite!')
