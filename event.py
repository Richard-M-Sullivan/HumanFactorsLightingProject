from queue import Queue

class Event:
    def __init__(self, queue=None, _type=None, data=None):
        self.queue = queue
        self._type = _type
        self.data = data

    def __str__(self):
        return f'queue:{self.queue}\ntype:{self._type}\ndata:{self.data}'

    def set_queue(self,queue):
        self.queue = queue

    def set_event(self,_type=None,data=None):
        self._type = _type
        self.data = data

    def push(self):
        if self.queue != None:
            self.queue.put(self)


def main():
    def event_handler(event):
        if event._type == 'cord' and event.data == 'up':
            new_event = Event(event.queue,'change_state','pig')
            new_event.push()
            print('event pushed')
        if event._type == 'change_state' and event.data == 'pig':
            print('we did it!')

    queue = Queue()

    event1 = Event(queue,'cord','up') 
    event1.push()
    print(event1)

    while queue.qsize() > 0:
        event_handler(queue.get())

if __name__ == '__main__':
    main()
