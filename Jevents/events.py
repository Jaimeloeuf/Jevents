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


def wait_for_daemons():
    """ Blocking function that waits for all the daemon threads to end by calling join
        method on them. If the thread is non-daemonic, join will not be called on it.
        It is fine as the python interpreter would not end the session when there is
        one or more non-daemonic threads alive. """

   # Loop till there are no daemonic threads left. Bigger than 1 as main thread is also counted.
    while len(threading.enumerate()) > 1:
        # Wait for all daemonic threads to end before ending the main thread, which will kill any still-alive daemonic threads.
        for thread in threading.enumerate():
            if thread.daemon:
                thread.join()
    """ Looping back up to check for daemonic threads again, because while waiting on the
        join statement, other threads may be able to spawn more new threads, which will be
        ignored Since the enumerate function only generates the list at the first call. """
