# default handler base class. does nothing to handle events
class StateHandler:
    def __init__(self,fsm,queue):
        self.name = 'default'
        self.queue = queue
        self.fsm = fsm

    def __str__(self):
        return f'{self.name}'

    def initialize(self, event=None):
        pass

    def handle_event(self, event):
        pass

# finite state machine handler, this is an event handler that delegates
# the responsibility of handling events to stateful event handlers, unless
# the event is to change states, then it changes which stateful handler it
# is using. To use this class one needs to add all the states to the
# state_registry, and then they will be able to switch between them with a
# call to handle_event, or with the set_state commnad
class FSMEventHandler:

    # initialize event handler with the default state handler
    def __init__(self, queue, state_handle=StateHandler):
        self.queue = queue
        self.state = None # this gets set to default state handler obj in set state
        self.state_registry = {}

        self.register_state(state_handle)
        self.set_state('default')

    # str prints the event handler and the current state that it is in
    def __str__(self):
        return f'FSMEventHandler:\n{str(self.state)}'

    # add the state to the state registry using the state's name as the key
    def register_state(self,state_handle):
        state = state_handle(self, self.queue)
        self.state_registry[state.name] = state

    # this sets the state of the handler by accessing a saved state in the
    # registry
    def set_state(self,state_name):
        self.state = self.state_registry[state_name]
        self.state.initialize()
    
    # handle event
    def handle_event(self,event):
            self.state.handle_event(event)

