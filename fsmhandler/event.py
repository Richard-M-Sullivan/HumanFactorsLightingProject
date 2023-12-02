from queue import Queue

class Event:
    def __init__(self, _type=None, data=None):
        self._type = _type
        self.data = data

    def __str__(self):
        return f'type:{self._type}\ndata:{self.data}'

    def set_event(self,_type=None,data=None):
        self._type = _type
        self.data = data

