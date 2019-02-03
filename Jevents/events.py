import threading


class EventEmitter(object):
    """	Class to emulate the use of EventEmitters in the Node JS runtime env.

        The last 3-lines of dunder code enables you to write your code like
            e += handler, e -= handler, e(earg)
        instead of
            e.add(handler), e.remove(handler), e.fire(earg).
    """
    def __init__(self):
        self.handlers = []
    
    def add(self, handler):
        self.handlers.append(handler)
        return self
    
    def remove(self, handler):
        self.handlers.remove(handler)
        return self
    
    def fire(self, sender, earg=None):
        for handler in self.handlers:
            handler(sender, earg)
    
    __iadd__ = add
    __isub__ = remove
    __call__ = fire


# Blocking function that waits for all the daemon threads to end by calling join method on them.
def wait_for_daemons():
    # Wait for all daemonic threads to end before ending the main thread, which will kill any still-alive daemonic threads.
    for thread in threading.enumerate():
        if thread.daemon:
            thread.join()