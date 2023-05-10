import json
import asyncio
from pandas import read_csv
from js import console, fetch, document, window, axios
from pyodide.ffi import create_proxy # Cria ao proxy 
from pyodide.http import open_url

LIMITE_MAX_CLIENTES = 30

url = "http://3.80.155.111/alldata"
FILE_PATH = '/Dados/USUARIOS_PETS_REPRESENTACAO_PERFIS.csv'
DATA_FRAME = read_csv(open_url(FILE_PATH), encoding='utf-8')

ELEMENTO_LOADER = document.getElementById('loader')
PAGINA_HOME = document.getElementById("fomulario-home")
PAGINA_RESPOSTA = document.getElementById("respota-div")
PAGINA_ERRO = document.getElementById("pagina-erro-div")

OL_ALIMENTOS = document.getElementById('ol-alimentos')
OL_BAZAR = document.getElementById("ol-bazar")
OL_HIGIENE = document.getElementById("ol-higiene-beleza")
PALAVRAS_RESEVADAS= {
    'CÃES': ['CÃES', 'OSSO', 'DOG', 'PEDIGREE', 'PUPPY', 'BULLDOG', 'CÃO', 'CAO', 'DOGUINHO'], 
    'GATOS': ['CAT', 'GATO', 'CATS', 'GATOS', 'WHISKAS'],
    
    'PÁSSAROS': ['PÁSSARO', 'PAPAGAIO' 'CALOPSITA', 'AVE', 'PERIQUITO', 'CURIO', 'PASSARO', 'SABIA', 'BEIJA FLOR', 'ALPISTE'],
    'RÉPTEIS': ['RÉPTEIS', 'RÉPTIL', 'JABUTI', 'TARTARUGA', 'TURTLE'],
    'PEIXES': ['PEIXE' 'AQUÁRIO', 'AQUA', 'FISH'],
    'ROEDORES':  ['ROEDOR', 'HAMSTER', 'COELHO', 'SERRAGEM', 'PORQUINHO'],
}

def getPalavrasResevadas(categoria):
    palavras = []
    for k,v in PALAVRAS_RESEVADAS.items():
        if(k != categoria):
            palavras += v
    console.log(str(palavras))
    return palavras



def iniciarLoader():
    ELEMENTO_LOADER.style.display = "block"
    PAGINA_HOME.style.filter = "blur(.2rem)"

def finalizarLoader():
    ELEMENTO_LOADER.style.display = "none"
    PAGINA_HOME.style.filter = "blur(0)"

async def solicitarIndicacao(payload):
        try:
            response = await axios.post(url,data=payload)
            data = response.data
            return data
        except Exception as e:
            navegarParaErro()
            console.log('Error:', e)

def getProdutos(proxy, categoria, palavrasReservas = []):
    produtos = []
    dictCategorias = dict(proxy.to_py())
    for item in dictCategorias[categoria]:
        presente = False
        nomeProduto = item['nome']
        for palavra in palavrasReservas:
            if palavra in nomeProduto:
                presente = True
                break
        if not presente:
            produtos.append(nomeProduto)
            
    return produtos

def listToLiStringHTML(list):
    html = ''
    for item in list:
        html += '<li>' + item + '</li>'
    return html

def navegarParaErro():
    ELEMENTO_LOADER.style.display = "none"
    PAGINA_HOME.style.display = "none"
    PAGINA_ERRO.style.display = "block"

def navegarParaResposta():
    PAGINA_HOME.style.display = "none"
    PAGINA_RESPOSTA.style.display = "block"

def montarResposta(data, listaPalavrasReservas):
    dados_retornados = data.result.data
    alimentos = listToLiStringHTML(getProdutos(dados_retornados, 'ALIMENTOS', listaPalavrasReservas))
    bazar = listToLiStringHTML(getProdutos(dados_retornados, 'BAZAR', listaPalavrasReservas))
    higiene = listToLiStringHTML(getProdutos(dados_retornados, 'HIGIENE E BELEZA', listaPalavrasReservas))

    OL_ALIMENTOS.innerHTML = alimentos
    OL_BAZAR.innerHTML = bazar
    OL_HIGIENE.innerHTML = higiene
    navegarParaResposta()


    
async def getData(*args):
    iniciarLoader()
    inpustDados = inputToJSON(['categoria', 'porte', 'idade'])
    categoriaSelecionada = inpustDados['categoria']
    listaPalavrasReservas = getPalavrasResevadas(categoriaSelecionada)

    especie_user, porte_user, idade_user = ler_entrada_usuario(inpustDados)
    clientes = identificar_perfis_iguais(especie_user, porte_user, idade_user)
    clientes = ordenarClientesPorProbabilidade(clientes)[:LIMITE_MAX_CLIENTES]
    codClientes = ",".join(str(x) for x in list(map(lambda x: x[0], clientes))) 
    payload = '{"profiles": [' + codClientes + ']}'
    data = await solicitarIndicacao(payload)

    montarResposta(data, listaPalavrasReservas)

    finalizarLoader()
    

async def main():
    await getData()
    

loop = asyncio.get_event_loop()
# loop.run_until_complete(main())




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


def identificar_perfis_iguais(especie_user, porte_user, idade_user):
    # Carrega o arquivo CSV usando o módulo pyodide.file_system
    df = DATA_FRAME
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
