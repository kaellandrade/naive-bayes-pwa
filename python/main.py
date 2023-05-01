import json
import asyncio
from js import console, fetch, document, window

from pyodide.ffi import create_proxy # Cria ao proxy 


url = "https://api.agify.io?name=meelad"

async def getData(*args):
    response = await fetch(url, {'method': 'GET'})
    json = await response.json()
    console.log('json', json)
    pre_element = document.createElement("h2")
    pre_element.textContent = str(json.age)
    my_div = document.getElementById("result")
    my_div.appendChild(pre_element)
    return json
    

async def main():
    await getData()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


#  =================================================

def f(*args):
    inputValues = document.getElementById('input-id').value
    console.log(inputValues)
    
def getValue():
    btn = document.getElementById('button-id')

    proxy_f = create_proxy(f, roundtrip=True)
    btn = document.getElementById('button-id')
    btn.addEventListener('click', proxy_f)
    

getValue()


# btn.removeEventListener('click', proxy_f)
# proxy_f.destroy()
