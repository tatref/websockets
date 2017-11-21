#!/usr/bin/env python

import asyncio
import datetime
import random
import websockets

async def time(websocket, path):
  print('Connection from ' + str(websocket.host) + ':' + str(websocket.port) + ', ' + str(websocket.secure))
  print('Path=' + str(path))

  #now = datetime.datetime.utcnow().isoformat() + 'Z'
  #websocket.send(now)

  while True:
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    await websocket.send(now)
    await asyncio.sleep(random.random() * 3)


listen_ip = '0.0.0.0'
listen_port = 5678

print('websocket listening on ' + str(listen_ip) + ':' + str(listen_port) + '...\n')

start_server = websockets.serve(time,listen_ip, listen_port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
