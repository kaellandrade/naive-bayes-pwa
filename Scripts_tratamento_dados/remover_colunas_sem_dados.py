import pandas as pd

# leitura do arquivo CSV
df = pd.read_csv('../Dados/DADOS_SEM_CLIENTES_1_2.csv')

# removendo as linhas com dados faltantes
df = df.drop(df[(df['ESPECIE'] == 'SEM ESPÉCIE') | (df['PORTE'] == 'SEM PORTE') | (df['IDADE'] == 'SEM IDADE')].index)

# salvando o novo arquivo CSV
df.to_csv('../Dados/DADOS_SEM_LINHAS_SEM_DADOS.csv', index=False)
