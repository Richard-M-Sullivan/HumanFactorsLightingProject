import asyncio
import random

def hello_world(loop):
    print('Hello World')
    loop.stop()

loop = asyncio.get_event_loop()
loop.call_soon(hello_world, loop)

loop.run_forever()
loop.close()
