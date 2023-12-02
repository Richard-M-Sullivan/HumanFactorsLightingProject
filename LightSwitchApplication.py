# standard lib includes 
import argparse
import asyncio
import random
import time

# imported tools
from fsmhandler.event import Event
from fsmhandler.fsm import FSMEventHandler
from fsmhandler.fsm import StateHandler
from queue import Queue as EventQueue

# custom states
from states.dim_timer_state import DimTimerState
from states.idlestate import IdleState
from states.toggle_timer_state import ToggleTimerState
from states.color_switcher import ColorSwitcherState
from states.dimmer_state import DimmerState

parser = argparse.ArgumentParser(description='program to control a light in home assistant')
parser.add_argument('-k', action='store_true', help='this option enables input from the spacebar')
args = parser.parse_args()

# conditional imports
if args.k:
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((300, 300))

    from keyboard_event_maker import KeyEventGenerator

else:
    from button_event_generator import ButtonEventGenerator


def calculate_delay(start_time):
    new_time = time.monotonic()
    delta_time = new_time - start_time
    delay = (1/60) - delta_time

    if delay < 0:
        return 0
    
    return delay
    

# create the event queue
event_queue = EventQueue()

#create event generator
event_generator = None
if args.k:
    event_generator = KeyEventGenerator(event_queue)
else:
    event_generator = ButtonEventGenerator(2,event_queue)

# create the event handler
event_handler = FSMEventHandler(event_queue)

# register states
event_handler.register_state(IdleState)
event_handler.register_state(DimTimerState)
event_handler.register_state(ToggleTimerState)
event_handler.register_state(ColorSwitcherState)
event_handler.register_state(DimmerState)

# set handler initial state
event_handler.set_state('idle')


while True:
    start_time = time.monotonic()
    # get input
    event_generator.generate_event()

    # process input
    while event_queue.qsize() > 0:
        event_handler.handle_event(event_queue.get())
    # sleep so the loop runs 60 times a second
    time.sleep(calculate_delay(start_time))
    
if args.k:
    pygame.quit()

