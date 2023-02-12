#!/usr/bin/env python

import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print("< {}".format(name))

    greeting = "Hello {}!".format(name)
    await websocket.send(greeting)
    print("> {}".format(greeting))

async def data(websocket, path):
    name = await websocket.recv()
    print("< {}".format(name))

    # reading file
    f = open('decision_file.txt','r') 
    y_hat = f.read()
    print(y_hat)
    f.close()

    await websocket.send(y_hat)
    print("> {}".format(y_hat))


start_server = websockets.serve(hello, '10.19.162.243', 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()