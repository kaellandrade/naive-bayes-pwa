import pandas as pd
import chardet

TAM_MAX_POR_PERFIL = 10


def remover_linhas_duplicadas(dataframe):
    """
    Função para ordenar descrecente o dataframe e pegar as 8 primeiras linhas e 2 ultimas
    """
    # Ordena o DataFrame com base na coluna 'REPRESENTACAO' em ordem decrescente
    df = dataframe.sort_values(by=['REPRESENTACAO'], ascending=False)

    # Seleciona as 8 primeiras linhas e 2 últimas linhas
    selecao = pd.concat([df.iloc[:8], df.iloc[-2:]])

    return selecao


# Descobrir a codificacao do csv
with open('../Dados/USUARIOS_PETS_REPRESENTACAO_FINAL.csv', 'rb') as f:
    encode = chardet.detect(f.read())

# Lê o arquivo CSV para um dataframe
df = pd.read_csv('../Dados/USUARIOS_PETS_REPRESENTACAO_FINAL.csv', encoding=encode['encoding'])

# Agrupa as linhas com base nas colunas "ESPECIE", "PORTE" e "IDADE"
grupos = df.groupby(['ESPECIE', 'PORTE', 'IDADE'])

# Itera sobre cada grupo
cont = 0
for nome_perfil, grupo in grupos:
    novo_dataframe = pd.DataFrame(grupo)
    if len(novo_dataframe) > TAM_MAX_POR_PERFIL:
        novo_dataframe = remover_linhas_duplicadas(novo_dataframe)
    # Adicionar o dataframe a um arquivo final csv
    if cont == 0:
        with open("../Dados/USUARIOS_PETS_REPRESENTACAO_PERFIS.csv", mode='a', newline='') as f:
            novo_dataframe.to_csv(f, header=True, index=False)
    else:
        with open("../Dados/USUARIOS_PETS_REPRESENTACAO_PERFIS.csv", mode='a', newline='') as f:
            novo_dataframe.to_csv(f, header=False, index=False)
    cont += 1

