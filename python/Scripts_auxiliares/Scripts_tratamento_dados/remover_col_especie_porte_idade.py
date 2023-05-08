import pandas as pd

df = pd.read_csv('../../../Dados/DADOS_TRATADOS_FINAL_SEM_FARMACIA.csv', encoding='utf-8')

# remove as colunas 'ESPECIE', 'PORTE' e 'IDADE'
df = df.drop(['ESPECIE', 'PORTE', 'IDADE'], axis=1)

# salva o DataFrame atualizado em um novo arquivo CSV
df.to_csv('../../../Dados/DADOS_TRATADOS_FINAL_2.csv', index=False)

