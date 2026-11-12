from pathlib import Path

#Crie a seguinte estrutura:

#├──dados/
#│  ├── entrada/
#│  └── saida/
#├──relatorios/

pasta_dados = Path('dados')
pasta_entrada = pasta_dados / 'entrada'
pasta_saida = pasta_dados / 'saida'
pasta_relatorios = Path('relatorios')

pasta_entrada.mkdir(parents=True, exist_ok=True)

pasta_saida.mkdir(parents=True, exist_ok=True)

pasta_relatorios.mkdir(parents=True, exist_ok=True)

pasta_dados = Path('dados')