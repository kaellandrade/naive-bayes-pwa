import pandas as pd
import chardet

FILE_1_PATH = '../Dados/Gabriel - inico a 10000/USUARIOS_PETS.csv'
FILE_2_PATH = '../Dados/Gabriel - inico a 10000/USUARIOS_IDADE.csv'

# Descobrir qual a codificação dos arquivos
with open(FILE_1_PATH, 'rb') as f:
    encode1 = chardet.detect(f.read())

with open(FILE_2_PATH, 'rb') as f:
    encode2 = chardet.detect(f.read())


# carregar arquivos CSV em DataFrames
df1 = pd.read_csv(FILE_1_PATH, encoding=encode1['encoding'])
df2 = pd.read_csv(FILE_2_PATH, encoding=encode2['encoding'])

# fazer merge dos DataFrames pela coluna CODCLI
df_merged = pd.merge(df1, df2, on='CODCLI')

# salvar resultado em um novo arquivo CSV
df_merged.to_csv('../Dados/Gabriel - inico a 10000/USUARIOS_PETS.csv', index=False)
