import json
import asyncio
from js import console, fetch, document, window, axios

from pyodide.ffi import create_proxy # Cria ao proxy 




url = "http://54.167.121.127/alldata"

async def getData(*args):
    # response = await fetch(url, {'method': 'GET'})
    # json = await response.json()
    # console.log('json', json)
    
    # return json
    payload = '{"profiles": [302501]}'

    try:
        response = await axios.post(url,data=payload)
        data = response.data
        console.log('data', data)
        return data
    except Exception as e:
        console.log('Error:', e)
    

async def main():
    await getData()

loop = asyncio.get_event_loop()
# loop.run_until_complete(main())


#  =================================================

def f(*args):
    inputValues = document.getElementById('input-id').value
    console.log(inputValues)

    
    
def getValue():
    btn = document.getElementById('button-id')

    proxy_f = create_proxy(getData, roundtrip=True)
    btn = document.getElementById('button-id')
    btn.addEventListener('click', proxy_f)
    
    

getValue()


# btn.removeEventListener('click', proxy_f)
# proxy_f.destroy()
