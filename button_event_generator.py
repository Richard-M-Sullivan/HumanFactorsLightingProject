from  event import Event
from gpiozero import Button

class ButtonEventGenerator:
    def __init__(self,pin,queue):
        self.button = Button(pin)
        self.queue = queue

        self.button.when_pressed = self.pressed_event
        self.button.when_released = self.released_event
        
    def pressed_event(self):
        new_event = Event('cord','down')
        self.queue.put(new_event)

    def released_event(self):
        new_event = Event('cord','down')
        self.queue.put(new_event)


