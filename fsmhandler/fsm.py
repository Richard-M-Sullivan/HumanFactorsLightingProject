# default handler base class. does nothing to handle events
class StateHandler:
    def __init__(self):
        self.name = 'default'

    def __str__(self):
        return f'{self.name}'

    def initialize(self):
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
    def __init__(self, state=StateHandler()):
        self.state = state
        self.state_registry = {}

        self.register_state(state)

    # str prints the event handler and the current state that it is in
    def __str__(self):
        return f'FSMEventHandler:\n{str(self.state)}'

    # add the state to the state registry using the state's name as the key
    def register_state(self,state):
        self.state_registry[state.name] = state

    # this sets the state of the handler by accessing a saved state in the
    # registry
    def set_state(self,state_name):
        self.state = self.state_registry[state_name]
        self.state.initialize()
    
    # handle event
    def handle_event(self,event):
        # if the event handler needs to change states, then handle event
        if event['type'] == 'change_state':
            self.set_state(event['data'])

        # otherwise delegate state handling to the state handler
        else:
            self.state.handle_event(event)




def main():

    ############################
    ## defining custom states ##
    ############################

    # happy state handler, prints name on initialization and happily handles
    # events
    class HappyState (StateHandler):
        def __init__(self):
            self.name = 'happy'

        def initialize(self):
            print(f'{self.name} initialized')

        def handle_event(self,event):
            print(f'event {event} happily handled')


    # sad state handler, prints name on initialization and sadly handles
    # events
    class SadState (StateHandler):
        def __init__(self):
            self.name = 'sad'

        def initialize(self):
            print(f'{self.name} initialized')

        def handle_event(self,event):
            print(f'event {event} sadly handled')


    # count state handler, prints name on initialization and counts handled
    # events
    class CountingState (StateHandler):
        def __init__(self):
            self.name = 'counting'
            self.count = 0

        def initialize(self):
            print(f'{self.name} initialized')

        def handle_event(self,event):
            self.count += 1
            print(f'events handled {self.count}')

    ############################
    ## start of main function ##
    ############################
    # create event handler
    event_handler = FSMEventHandler()

    # create and register events
    event_handler.register_state(HappyState())
    event_handler.register_state(SadState())
    event_handler.register_state(CountingState())

    # set the happy state
    event_handler.set_state('happy')

    # test if happy handles event
    event_handler.handle_event({'type':'wow','data':'super cool'})

    # test if change to sad event works
    event_handler.handle_event({'type':'change_state', 'data':'sad'})

    # test if sad handles event
    event_handler.handle_event({'type':'wow','data':'super cool'})

    # change to counting state
    event_handler.handle_event({'type':'change_state','data':'counting'})

    # test if counting works
    event_handler.handle_event({'type':'wow','data':'super cool'})
    event_handler.handle_event({'type':'wow','data':'super cool'})
    event_handler.handle_event({'type':'wow','data':'super cool'})

    # switch to sad
    event_handler.handle_event({'type':'change_state', 'data':'sad'})
    event_handler.handle_event({'type':'wow','data':'super cool'})

    # switch back to counting and see if works
    event_handler.handle_event({'type':'change_state','data':'counting'})
    event_handler.handle_event({'type':'wow','data':'super cool'})
    event_handler.handle_event({'type':'wow','data':'super cool'})
    event_handler.handle_event({'type':'wow','data':'super cool'})

if __name__ == '__main__':
    main()

