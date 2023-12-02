from  fsmhandler.event import Event
from gpiozero import Button

class ButtonEventGenerator:
    def __init__(self,pin,queue):
        self.button = Button(pin)
        self.queue = queue
        self.state = self.button.is_pressed

    def generate_event(self):
        current_state = self.button.is_pressed

        if self.state == current_state:
            return
        
        self.state = current_state

        if self.state == True:
            self.pressed_event()
        else:
            self.released_event()

    def pressed_event(self):
        new_event = Event('cord','down')
        self.queue.put(new_event)
        print('down event')

    def released_event(self):
        new_event = Event('cord','up')
        self.queue.put(new_event)
        print('up event')


