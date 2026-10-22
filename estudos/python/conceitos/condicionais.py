#senha = '1234'
#tentativa = input('Digite a senha: ')
#if tentativa == senha:
    #print('Acesso permitido')

#if tentativa != senha:
    #print('Acesso negado')

#------------------------

# MATCH CASE

nota = float(input('Digite sua nota: '))

match nota:
    case 10:
        print('Excelente!')

    case 9:
        print('Muito bom!')

    case 8:
        print('Bom!')

    case 7:
        print('Regular!')
        
    case _:
        print('Nota inválida!')
