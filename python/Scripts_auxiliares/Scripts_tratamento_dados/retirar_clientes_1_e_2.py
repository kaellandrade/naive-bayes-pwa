import pandas as pd

dados = pd.read_csv('../Dados/DADOS_SEM_EAN.csv')
dados_filtrados = dados[(dados['CODCLI'] != 1) & (dados['CODCLI'] != 2)]
dados_filtrados.to_csv('../Dados/DADOS_TRATADOS.csv', index=False)