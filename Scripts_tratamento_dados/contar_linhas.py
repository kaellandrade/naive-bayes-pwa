import pandas as pd

# Lê o arquivo CSV
df = pd.read_csv("../Dados/DADOS_BRUTOS.csv")

# Conta o número de linhas
num_linhas1 = len(df)

# Imprime o resultado
print("Número de linhas:", num_linhas1)


df = pd.read_csv("../Dados/DADOS_NOVAS_CARACTERISTICAS.csv")
num_linhas2 = len(df)
print("Número de linhas:", num_linhas2)

print("Número de linhas 1 - Número de linhas 2:", num_linhas1 - num_linhas2)