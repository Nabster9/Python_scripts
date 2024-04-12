import asyncio
import websockets
async def test():
    async with websockets.connect('ws://pt****.libcurl.so/pentesterlab') as websocket:
        await websocket.send("key")
        response = await websocket.recv()
        print(response)
asyncio.get_event_loop().run_until_complete(test())