import pandas as pd

# Lê o arquivo CSV para um dataframe
df = pd.read_csv('../Dados/USUARIOS_PETS_REPRESENTACAO_PERFIS.csv', encoding='utf-8')

# salvando o novo arquivo CSV
df.to_csv('../Dados/USUARIOS_PETS_REPRESENTACAO_PERFIS_2.csv', header=True, encoding='utf-8', index=False)
