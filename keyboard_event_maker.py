import pygame

from event import Event
from pygame.key import get_pressed
from pygame.locals import *
from queue import Queue

class KeyEventGenerator:
    def __init__(self,queue):
        self.current_state = get_pressed()[K_SPACE]
        self.queue = queue

        print(self.current_state)

    def generate_event(self):
        # go through pygame events and get the spacebar events
        event_found = False
        string_state = None
        for event in pygame.event.get():

            if event.type == KEYUP and event.key == K_SPACE:
                string_state = 'up'
                event_found = True

            elif event.type == KEYDOWN and event.key == K_SPACE:
                string_state = 'down'
                event_found = True


            if event_found:
                event_found = False
                
                new_event = Event('cord', string_state)
                self.queue.put(new_event)




