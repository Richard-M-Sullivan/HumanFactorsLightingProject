import asyncio

from event import Event
from fsmhandler.fsm import StateHandler

class ColorSwitcherState (StateHandler):
    def __init__(self, fsm, queue):
        self.name = 'color_switcher'
        self.fsm = fsm
        self.queue = queue

        self.current_color = 0
        self.colors = [
            'white',
            'red',
            'orange',
            'yellow',
            'green',
            'blue',
            'indigo',
            'violet',
        ]
        

    def initialize(self):
        self.change_color()


    def handle_event(self, event):
        if event._type == 'cord' and event.data == 'down':
            self.change_color()

        elif event._type == 'cord' and event.data == 'up':
            print(f'cord up, need to toggle color timer')

        elif event._type == 'timer' and event.data == 'color':
            print(f'timer color, need to set state to idle')
            self.fsm.set_state('idle')

        else:
            print(f'event not handled by me bro')


    def push_timer_event(self):
        new_event = Event('timer','toggle')
        self.queue.put(new_event)


    def change_color(self):
        self.current_color = (self.current_color + 1) % len(self.colors)
        print(f'color set to {self.colors[self.current_color]}')

