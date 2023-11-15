from event import Event
from fsmhandler.fsm import StateHandler

class IdleState (StateHandler):
    def __init__(self, fsm, queue):
        self.name = 'idle'
        self.fsm = fsm
        self.queue = queue

    def initialize(self):
        pass

    def handle_event(self, event):
        if event._type == 'cord' and event.data == 'down':
            print(f'cord down, so set state to dim_timer')
            self.fsm.set_state('dim_timer')

        else:
            print(f'event not handled by me bro')

