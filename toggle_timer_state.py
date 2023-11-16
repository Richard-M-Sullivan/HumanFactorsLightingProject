
from event import Event
from fsmhandler.fsm import StateHandler
from threading import Timer

class ToggleTimerState (StateHandler):
    def __init__(self, fsm, queue):
        self.name = 'toggle_timer'
        self.fsm = fsm
        self.queue = queue
        self.dim_timer = None


    def initialize(self):
        self.dim_timer = Timer(0.7,self.push_timer_event)
        self.dim_timer.start()


    def handle_event(self, event):
        if event._type == 'cord' and event.data == 'down':
            self.dim_timer.cancel()
            self.fsm.set_state('color_switcher')

        elif event._type == 'timer' and event.data == 'toggle':
            print('toggling light\n')
            self.fsm.set_state('idle')


    def push_timer_event(self):
        new_event = Event('timer','toggle')
        self.queue.put(new_event)


