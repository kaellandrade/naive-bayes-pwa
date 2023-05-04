import pandas as pd

# Lê o arquivo CSV para um dataframe
df = pd.read_csv('../Dados/DADOS_TRATADOS_SEM_REPETIR_PRODUTO.csv', encoding='utf-8')

# removendo as linhas com dados faltantes
df = df.drop(df[(df['ESPECIE'] == 'SEM ESPECIE') | (df['PORTE'] == 'SEM PORTE') | (df['IDADE'] == 'SEM IDADE')].index)

# salvando o novo arquivo CSV
df.to_csv('../Dados/DADOS_TRATADOS_FINAL.csv', index=False)
