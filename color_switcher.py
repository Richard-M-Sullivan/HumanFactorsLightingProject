import light_controller

from event import Event
from fsmhandler.fsm import StateHandler
from threading import Timer

class ColorSwitcherState (StateHandler):
    def __init__(self, fsm, queue):
        self.name = 'color_switcher'
        self.fsm = fsm
        self.queue = queue
        self.color_timer = None

        self.current_color = 0
        self.colors = [
            'white',
            'red',
            'orange',
            'yellow',
            'green',
            'blue',
            'purple',
            'pink',
        ]
        

    def initialize(self):
        print('swithing colors\n')
        self.change_color()


    def handle_event(self, event):
        if event._type == 'cord' and event.data == 'down':
            self.color_timer.cancel()
            self.change_color()

        elif event._type == 'cord' and event.data == 'up':
            self.color_timer = Timer(0.75, self.push_timer_event)
            self.color_timer.start()

        elif event._type == 'timer' and event.data == 'color':
            print()
            self.fsm.set_state('idle')


    def push_timer_event(self):
        new_event = Event('timer','color')
        self.queue.put(new_event)


    def change_color(self):
        self.current_color = (self.current_color + 1) % len(self.colors)
        light_controller.trigger_endpoint(self.colors[self.current_color])
        print(f'color set to {self.colors[self.current_color]}')

