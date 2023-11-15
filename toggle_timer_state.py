
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
        print('starting toggle timer')
        self.dim_timer = Timer(0.5,self.push_timer_event)
        self.dim_timer.start()


    def handle_event(self, event):
        if event._type == 'cord' and event.data == 'down':
            print(f'cord down, set state to color_switcher')
            self.dim_timer.cancel()
            self.fsm.set_state('color_switcher')

        elif event._type == 'timer' and event.data == 'toggle':
            print(f'timer toggle, need to toggle light and set state to idle')
            self.fsm.set_state('idle')
            
        else:
            print(f'event not handled by me bro')


    def push_timer_event(self):
        new_event = Event('timer','toggle')
        self.queue.put(new_event)


