import pandas as pd
from unidecode import unidecode
import chardet

FILE_2_PATH = '../Dados/USUARIOS_PETS_REPRESENTACAO_PERFIS.csv'

with open(FILE_2_PATH, 'rb') as f:
    encode2 = chardet.detect(f.read())

# carregar arquivos CSV em DataFrames
df = pd.read_csv(FILE_2_PATH, encoding=encode2['encoding'])

# Colunas que desejam remover os acentos
cols = ['ESPECIE', 'PORTE', 'IDADE']

# Aplicando a função unidecode() em cada coluna
df[cols] = df[cols].apply(lambda x: x.apply(unidecode))

# Salvando o arquivo CSV sem acentos
df.to_csv('../Dados/USUARIOS_PETS_REPRESENTACAO_PERFIS_2.csv', index=False)
