import json
import asyncio
from js import console, fetch, document, window
import pandas
from pyodide.ffi import create_proxy # Cria ao proxy 

LIMITE_MAX_CLIENTES = 15

url = "https://api.agify.io?name=meelad"

async def getData(*args):
    inpustDados = inputToJSON(['categoria', 'porte', 'idade'])
    console.log(str(inpustDados))

    especie_user, porte_user, idade_user = ler_entrada_usuario(inpustDados)
    clientes = await identificar_perfis_iguais(especie_user, porte_user, idade_user)
    clientes = ordenarClientesPorProbabilidade(clientes)[:LIMITE_MAX_CLIENTES]
    console.log(clientes)


    # return json
    

async def main():
    await getData()
    

loop = asyncio.get_event_loop()
# loop.run_until_complete(main())


#  =================================================

def f(*args):
    inputValues = document.getElementById('input-id').value
    console.log(inputValues)

    
    
def getValue():
    btn = document.getElementById('btn-enviar')

    proxy_f = create_proxy(getData, roundtrip=True)
    btn = document.getElementById('btn-enviar')
    btn.addEventListener('click', proxy_f)
    
    

def inputToJSON(list):
    values = {}
    def getChecked(stringCampo):
        stringSlector = 'input[name^=\"'+stringCampo+'\"]'
        listaInputs = document.querySelectorAll(stringSlector)
        for i in listaInputs:
            if(i.checked):
                return i.value
    for i in list:
       values[i] =  getChecked(i)
       
    
    
    return values


getValue()

# btn.removeEventListener('click', proxy_f)
# proxy_f.destroy()

def ler_entrada_usuario(entrada):
    especie_in = entrada['categoria']
    porte_in = entrada['porte']
    idade_in = entrada['idade']
    return especie_in, porte_in, idade_in

def splitDados(df, row):
    cliente = df.iloc[row]['CODCLI']
    especie = df.iloc[row]['ESPECIE']
    porte = df.iloc[row]['PORTE']
    idade = df.iloc[row]['IDADE']
    probabilidade = df.iloc[row]['REPRESENTACAO']
    probabilidade = float(probabilidade.replace('%', ''))
    return cliente, especie, porte, idade, probabilidade

async def abrirArquivo():
    zipResponse = await fetch("http://127.0.0.1:5500/USUARIOS_PETS_REPRESENTACAO_PERFIS.csv");
    return zipResponse.unpack_archive()

async def identificar_perfis_iguais(especie_user, porte_user, idade_user):
    # Lê o arquivo CSV para um dataframe
    console.log('antes do fettch')
    caminho_arquivo = '../USUARIOS_PETS_REPRESENTACAO_PERFIS.csv'
    df = pandas.read_csv(caminho_arquivo, encoding='utf-8')
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
