# standard lib includes 
import asyncio
import pygame
import random
import time

# imported tools
from event import Event
from fsmhandler.fsm import FSMEventHandler
from fsmhandler.fsm import StateHandler
from keyboard_event_maker import KeyEventGenerator
from queue import Queue as EventQueue

# custom states
from dim_timer_state import DimTimerState
from idlestate import IdleState
from toggle_timer_state import ToggleTimerState
from color_switcher import ColorSwitcherState

def calculate_delay(start_time):
    new_time = time.monotonic()
    delta_time = new_time - start_time
    delay = (1/60) - delta_time

    if delay < 0:
        return 0
    
    return delay
    
pygame.init()

# create the event queue
event_queue = EventQueue()

#create keyboard event generator
keyboard_event_generator = KeyEventGenerator(event_queue)

# create the event handler
event_handler = FSMEventHandler(event_queue)

# register states
event_handler.register_state(IdleState)
event_handler.register_state(DimTimerState)
event_handler.register_state(ToggleTimerState)
event_handler.register_state(ColorSwitcherState)

# set handler initial state
event_handler.set_state('idle')

# create events
random_event = Event('wow','super cool')
cord_down = Event('cord','down')
cord_up = Event('cord','up')

for i in range(60*30):
    start_time = time.monotonic()
    # get input
    keyboard_event_generator.generate_event()
    pygame.event.pump()
    # process input
    while event_queue.qsize() > 0:
        event_handler.handle_event(event_queue.get())
    # sleep so the loop runs 60 times a second
    time.sleep(calculate_delay(start_time))
    
pygame.quit()

