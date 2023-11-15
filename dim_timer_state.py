import asyncio

from event import Event
from fsmhandler.fsm import StateHandler

class DimTimerState (StateHandler):
    def __init__(self, fsm, queue):
        self.name = 'dim_timer'
        self.fsm = fsm
        self.queue = queue


    def initialize(self):
        print('need to start timer')


    def handle_event(self, event):
        if event._type == 'cord' and event.data == 'up':
            print(f'cord up, set state to toggle_timer')
            self.fsm.set_state('toggle_timer')

        elif event._type == 'timer' and event.data == 'dimmer':
            print(f'timer dimmer, set state to dimmer')
            self.fsm.set_state('dimmer')
            
        else:
            print(f'event not handled by me bro')


    def push_timer_event(self):
        new_event = Event('timer','dimmer')
        self.queue.put(new_event)

