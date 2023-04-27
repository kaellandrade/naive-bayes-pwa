import pandas as pd

# leitura do arquivo CSV
df = pd.read_csv('../Dados/DADOS_SEM_LINHAS_SEM_DADOS.csv')

# criando as novas colunas relacionadas a idade
df['IS_FILHOTE'] = df['IDADE'].str.contains('FILHOTE').astype(int)
df['IS_ADULTO'] = df['IDADE'].str.contains('ADULTO').astype(int)
df['IS_SENIOR'] = df['IDADE'].str.contains('SÊNIOR').astype(int)

# criando as novas colunas relacionadas a especie
df['IS_CAO'] = df['ESPECIE'].str.contains('CÃES').astype(int)
df['IS_GATO'] = df['ESPECIE'].str.contains('GATOS').astype(int)
df['IS_PEIXES'] = df['ESPECIE'].str.contains('PEIXES').astype(int)
df['IS_PASSARO'] = df['ESPECIE'].str.contains('PÁSSAROS').astype(int)
df['IS_ROEDOR'] = df['ESPECIE'].str.contains('ROEDORES').astype(int)
df['IS_REPTIL'] = df['ESPECIE'].str.contains('RÉPTEIS').astype(int)

# criando as novas colunas relacionadas ao porte
df['IS_PEQUENO'] = df['PORTE'].str.contains('PEQUENO').astype(int)
df['IS_MEDIO'] = df['PORTE'].str.contains('MÉDIO').astype(int)
df['IS_GRANDE'] = df['PORTE'].str.contains('GRANDE').astype(int)
df['IS_GIGANTE'] = df['PORTE'].str.contains('GIGANTE').astype(int)

# Excluindo as colunas ESPECIE, PORTE e IDADE
df = df.drop(columns=["ESPECIE", "PORTE", "IDADE"])

# salvando o novo arquivo CSV
df.to_csv('../Dados/DADOS_NOVAS_CARACTERISTICAS.csv', index=False)
