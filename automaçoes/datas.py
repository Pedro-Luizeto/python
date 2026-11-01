#from datetime import datetime

#agora = datetime.now()
#print(agora)
#print(agora.day)

##agora = datetime.now()

#print(agora.strftime('Hojé é dia %d do mês %m do ano %Y.'))

#print(agora.strftime('Hojé é dia são %H:%M:%S.'))

#data_str = "2024-06-15 14:30:00"

#data_convertida = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")
#print(data_convertida)

# -------------------- PARTE 2 --------------------


from datetime import datetime, timedelta

#hoje = datetime.now()
#um_dia = timedelta(days=1)
#ontem = hoje - um_dia
#amanha = hoje + um_dia
#print(f"Hoje é {hoje.strftime('%d/%m/%Y')}, e amanhã será {amanha.strftime('%d/%m/%Y')}.")

#prazo = datetime(2025, 7, 24)
#hoje = datetime.now()

#if hoje < prazo:
    #dias_restantes = (prazo - hoje).days
    #print(f"Faltam {dias_restantes} dias para o prazo final.")

#else:
    #print("O prazo final já passou.")

aniversario = datetime(2027, 8, 17)
hoje = datetime.now()

if aniversario > hoje:
    dias_ate_aniversario = (aniversario - hoje).days
    print(f"Faltam {dias_ate_aniversario} dias para o meu aniversário.")

elif aniversario < hoje:
    print("Meu aniversário já passou este ano.")

elif aniversario.day == hoje.day and aniversario.month == hoje.month:
    print("Hoje é meu aniversário!")