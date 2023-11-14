from fsmhandler.fsm import StateHandler

class IdleState (StateHandler):
    def __init__(self):
        self.name = 'idle'

    def initialize(self):
        pass

    def handle_event(self, event):
        if event['type'] == 'cord' and event['data'] == 'down':
            event = {'type':'change_state','data':'dim_timer'}
            print(f'new event {event}')

        else:
            print(f'event not handled by me bro')

