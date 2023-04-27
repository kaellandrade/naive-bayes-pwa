import json
import asyncio
from js import console, fetch, document, window

import js


url = "https://api.agify.io?name=meelad"

async def getData():
    response = await fetch(url, {'method': 'GET'})
    json = await response.json()
    console.log('json', json)
    

async def main():
    await getData()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
