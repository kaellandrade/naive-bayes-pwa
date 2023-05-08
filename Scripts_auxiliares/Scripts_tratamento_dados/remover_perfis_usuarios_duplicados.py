import pandas as pd

df = pd.read_csv('../Dados/USUARIOS_PETS_REPRESENTACAO_FINAL.csv')

# Ordena o DataFrame com base na coluna 'REPRESENTACAO' em ordem decrescente
df = df.sort_values(by=['REPRESENTACAO'], ascending=False)

# Remover linhas duplicadas, escolhendo salvar a primeira ocorrencia, que será a de maior representação
df.drop_duplicates(subset=['ESPECIE', 'PORTE', 'IDADE'], keep='first', inplace=True)

df.to_csv('../Dados/USUARIOS_PETS_REPRESENTACAO_DUP.csv', index=False)
