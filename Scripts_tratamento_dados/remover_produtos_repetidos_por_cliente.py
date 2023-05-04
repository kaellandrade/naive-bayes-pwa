import pandas as pd

# Lendo o arquivo CSV original
df_dados_tratados = pd.read_csv("../Dados/DADOS_TRATADOS.csv")

# cria um dataframe com uma coluna chamada 'valores'
df_usuarios = pd.read_csv("../Dados/USUARIOS.csv")

# itera sobre cada linha do dataframe e imprime o valor da coluna 'valores'
cont = 1
for index, row in df_usuarios.iterrows():
    cliente = row['CODCLI']

    # Criando um novo dataframe apenas com as linhas que possuem CODCLI igual a x
    df_x = df_dados_tratados[df_dados_tratados["CODCLI"] == cliente].copy()

    # Removendo as linhas onde a coluna "PRODUTO" se repete
    df_x.drop_duplicates(subset=["PRODUTO"], inplace=True)

    # Adicionar as novas linhas ao final do arquivo existente
    with open("../Dados/DADOS_TRATADOS_SEM_REPETIR_PRODUTO.csv", mode='a', newline='') as f:
        df_x.to_csv(f, header=False, index=False)

    print(cont)
    cont += 1

