import pandas as pd
import sys

# Leitura do CSV
df = pd.read_csv('./Dados/DADOS_TRATADOS.csv')

# Seleciona as linhas que contêm o valor Y na coluna X
cliente = int(sys.argv[1])
# cliente = 305985
df_Y = df[df['CODCLI'] == cliente]

# Salva as linhas selecionadas em um novo CSV
df_Y.to_csv('./Dados/DADOS_CLIENTE_X.csv', index=False)
