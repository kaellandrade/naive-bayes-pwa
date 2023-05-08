import pandas as pd

# Define o número de linhas aleatórias que você quer selecionar
num_linhas_aleatorias = 1000

# Lê o arquivo CSV usando o pandas
df = pd.read_csv('./Dados/DADOS_NOVAS_CARACTERISTICAS.csv')

# Seleciona um número x de linhas aleatórias
linhas_aleatorias = df.sample(n=num_linhas_aleatorias)

# Cria um novo arquivo CSV com as linhas selecionadas
linhas_aleatorias.to_csv('./Dados/DADOS_TESTE_MIL.csv', index=False)
