import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('./Dados/DADOS_TRATADOS.csv')

# Selecionar a coluna 'CODCLI' e remover valores duplicados
codcli_unique = df['CODCLI'].unique()

# Criar um novo DataFrame com a coluna 'CODCLI' contendo valores únicos
df_unique = pd.DataFrame({'CODCLI': codcli_unique})

# Salvar os valores únicos em um novo arquivo CSV
df_unique.to_csv('./Dados/USUARIOS.csv', index=False)
