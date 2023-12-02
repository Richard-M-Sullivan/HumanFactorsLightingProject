from fsmhandler.event import Event
from fsmhandler.fsm import StateHandler

class IdleState (StateHandler):
    def __init__(self, fsm, queue):
        self.name = 'idle'
        self.fsm = fsm
        self.queue = queue

    def initialize(self):
        print('idle\n')

    def handle_event(self, event):
        if event._type == 'cord' and event.data == 'down':
            self.fsm.set_state('dim_timer')

