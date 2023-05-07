import json
import asyncio
from js import console, fetch, document, window

from pyodide.ffi import create_proxy # Cria ao proxy 


url = "https://api.agify.io?name=meelad"

async def getData(*args):
    inpustDados = inputToJSON(['categoria', 'porte', 'idade'])
    console.log(inpustDados)
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
       
    
    
    return str(values)


getValue()

# btn.removeEventListener('click', proxy_f)
# proxy_f.destroy()
