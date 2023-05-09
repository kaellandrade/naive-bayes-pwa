import pandas as pd
import sys

LIMITE_MAX_CLIENTES = 15

def ler_entrada_usuario():
    especie_in = porte_in = idade_in = ""

    print("Escolha a espécie:")
    print("\t1: CÃES\n\t2: GATOS\n\t3: RÉPTEIS\n\t4: PÁSSAROS\n\t5: ROEDORES")
    resp = input()
    if resp == '1':
        especie_in = "CÃES"
    elif resp == '2':
        especie_in = "GATOS"
    elif resp == '3':
        especie_in = "RÉPTEIS"
    elif resp == '4':
        especie_in = "PÁSSAROS"
    elif resp == '5':
        especie_in = "ROEDORES"

    print("Escolha o porte:")
    print("\t1: PEQUENO\n\t2: MÉDIO\n\t3: GRANDE\n\t4: GIGANTE")
    resp = input()
    if resp == '1':
        porte_in = "PEQUENO"
    elif resp == '2':
        porte_in = "MÉDIO"
    elif resp == '3':
        porte_in = "GRANDE"
    elif resp == '4':
        porte_in = "GIGANTE"

    print("Escolha a idade:")
    print("\t1: FILHOTE\n\t2: ADULTO\n\t3: SÊNIOR")
    resp = input()
    if resp == '1':
        idade_in = "FILHOTE"
    elif resp == '2':
        idade_in = "ADULTO"
    elif resp == '3':
        idade_in = "SÊNIOR"

    return especie_in, porte_in, idade_in

def splitDados(df, row):
    cliente = df.iloc[row]['CODCLI']
    especie = df.iloc[row]['ESPECIE']
    porte = df.iloc[row]['PORTE']
    idade = df.iloc[row]['IDADE']
    probabilidade = df.iloc[row]['REPRESENTACAO']
    probabilidade = float(probabilidade.replace('%', ''))
    return cliente, especie, porte, idade, probabilidade

def identificar_perfis_iguais(especie_user, porte_user, idade_user):
    # Lê o arquivo CSV para um dataframe
    df = pd.read_csv('../Dados/USUARIOS_PETS_REPRESENTACAO_PERFIS.csv', encoding='utf-8')
    clientes_iguais = []
    for row in range(len(df)):
        cliente, especie, porte, idade, probabilidade = splitDados(df, row)
        if especie_user == especie and porte_user == porte and idade_user == idade:
            clientes_iguais.append((cliente, probabilidade))

    if len(clientes_iguais) == 0:
        for row in range(len(df)):
            cliente, especie, porte, idade, probabilidade = splitDados(df, row)
            if especie_user in especie and porte_user == porte and idade_user == idade:
                clientes_iguais.append((cliente, probabilidade))
    if len(clientes_iguais) == 0:
        for row in range(len(df)):
            cliente, especie, porte, idade, probabilidade = splitDados(df, row)
            if especie_user in especie and porte_user in porte and idade_user == idade:
                clientes_iguais.append((cliente, probabilidade))
    if len(clientes_iguais) == 0:
        for row in range(len(df)):
            cliente, especie, porte, idade, probabilidade = splitDados(df, row)
            if especie_user in especie and porte_user in porte and idade_user in idade:
                clientes_iguais.append((cliente, probabilidade))

    return clientes_iguais


def ordenarClientesPorProbabilidade(array_clientes):
    return sorted(array_clientes, key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    especie_user, porte_user, idade_user = ler_entrada_usuario()
    clientes = identificar_perfis_iguais(especie_user, porte_user, idade_user)
    clientes = ordenarClientesPorProbabilidade(clientes)[:LIMITE_MAX_CLIENTES]
    print(clientes)

