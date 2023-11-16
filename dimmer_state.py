from event import Event
from fsmhandler.fsm import StateHandler
from threading import Timer

class DimmerState (StateHandler):
    def __init__(self, fsm, queue):
        self.name = 'dimmer'
        self.fsm = fsm
        self.queue = queue
        self.brightness = 0
        self.MAX_BRIGHTNESS = 255
        self.dimmer_timer = None

    def initialize(self):
        print('dimming\n')
        self.brightness = 0
        self.dim_light()

        self.dimmer_timer = Timer(0.75, self.push_timer_event)
        self.dimmer_timer.start()


    def handle_event(self, event):
        if event._type == 'cord' and event.data == 'up':
            print()
            self.fsm.set_state('idle')

        elif event._type == 'timer' and event.data == 'dimmer':
            self.dim_light()
            self.dimmer_timer = Timer(1, self.push_timer_event)
            self.dimmer_timer.start()


    def push_timer_event(self):
        new_event = Event('timer','dimmer')
        self.queue.put(new_event)


    def dim_light(self):
        self.brightness = self.brightness+10 if self.brightness+10 < 255 else 0
        print(f'brightness set to {self.brightness}')


