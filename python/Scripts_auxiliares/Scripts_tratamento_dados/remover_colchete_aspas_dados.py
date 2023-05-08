import pandas as pd
import chardet

FILE_PATH = '../Dados/Gabriel - inico a 10000/USUARIOS_PETS.csv'

# Descobrir qual a codificação dos arquivos
with open(FILE_PATH, 'rb') as f:
    encode1 = chardet.detect(f.read())

# carregar arquivos CSV em DataFrames
df = pd.read_csv(FILE_PATH, encoding=encode1['encoding'])

df = df.applymap(lambda x: str(x).replace("[", "").replace("]", "").replace("'", ""))
df.to_csv('../Dados/Gabriel - inico a 10000/USUARIOS_PETS.csv', index=False)
