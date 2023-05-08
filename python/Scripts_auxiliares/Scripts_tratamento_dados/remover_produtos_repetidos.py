import pandas as pd
import chardet

# Lendo o arquivo CSV original
with open("../Dados/DADOS_TRATADOS_SEM_REPETIR_PRODUTO.csv", 'rb') as f:
    encode = chardet.detect(f.read())

df = pd.read_csv("../Dados/DADOS_TRATADOS_SEM_REPETIR_PRODUTO.csv", encoding=encode['encoding'])

# Removendo as linhas onde a coluna "CODPROD" se repete
df.drop_duplicates(subset=["CODPROD"], keep='last', inplace=True)

df.to_csv("../Dados/DADOS_TRATADOS_SEM_REPETIR_PRODUTO_GERAL.csv", index=False)


