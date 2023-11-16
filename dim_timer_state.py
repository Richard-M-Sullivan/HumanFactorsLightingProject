
from event import Event
from fsmhandler.fsm import StateHandler
from threading import Timer

class DimTimerState (StateHandler):
    def __init__(self, fsm, queue):
        self.name = 'dim_timer'
        self.fsm = fsm
        self.queue = queue
        self.dim_timer = None


    def initialize(self):
        self.dim_timer = Timer(0.75,self.push_timer_event)
        self.dim_timer.start()


    def handle_event(self, event):
        if event._type == 'cord' and event.data == 'up':
            self.dim_timer.cancel()
            self.fsm.set_state('toggle_timer')

        elif event._type == 'timer' and event.data == 'dimmer':
            self.fsm.set_state('dimmer')


    def push_timer_event(self):
        new_event = Event('timer','dimmer')
        self.queue.put(new_event)

