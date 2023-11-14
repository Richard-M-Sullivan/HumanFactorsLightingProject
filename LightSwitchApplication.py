import asyncio
import random

from fsmhandler.fsm import FSMEventHandler
from fsmhandler.fsm import StateHandler
from idlestate import IdleState

def hello_world(loop):
    print('Hello World')
    loop.stop()

loop = asyncio.get_event_loop()
loop.call_soon(hello_world, loop)

loop.run_forever()
loop.close()


event_handler = FSMEventHandler()

event_handler.register_state(IdleState())

event_handler.set_state('idle')

event_handler.handle_event({'type':'wow','data':'super cool'})
event_handler.handle_event({'type':'cord','data':'up'})
event_handler.handle_event({'type':'wow','data':'super cool'})
event_handler.handle_event({'type':'cord','data':'down'})
event_handler.handle_event({'type':'wow','data':'super cool'})
event_handler.handle_event({'type':'cord','data':'up'})
event_handler.handle_event({'type':'wow','data':'super cool'})
event_handler.handle_event({'type':'cord','data':'down'})
event_handler.handle_event({'type':'wow','data':'super cool'})

