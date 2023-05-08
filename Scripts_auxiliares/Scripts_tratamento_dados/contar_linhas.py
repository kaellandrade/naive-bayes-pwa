import pandas as pd
import chardet

with open("../Dados/DADOS_TRATADOS_SEM_REPETIR_PRODUTO.csv", 'rb') as f:
    encode = chardet.detect(f.read())

# carregar arquivos CSV em DataFrames
df = pd.read_csv("../Dados/DADOS_TRATADOS_SEM_REPETIR_PRODUTO.csv", encoding=encode['encoding'])


# Conta o número de linhas
num_linhas1 = len(df)

# Imprime o resultado
print("Número de linhas:", num_linhas1)

