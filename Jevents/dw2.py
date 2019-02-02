from threading import Thread


class Watch:
    """ Watch class to implement a data-observer pattern on the encapsulated data item.
        The event-handlers/callbacks will be ran when the data is changed/set. """

    def __init__(self, data):
        """ Pass constructor the data item to be watched """
        self.__data = data
        self.on_set = callbacks()
        self.on_change = callbacks()

    # Method to set a value to the data variable watched by this class
    def set(self, data):
        # If set is called and data value has been changed, save the data and run on change callbacks
        if data != self.__data:  # Check for data equality, so will not work for object references
            self.__data = data
            # Call all the __on_change_cbs callback functions
            self.__event(self.on_change.get)

        # Regardless of data, call all the __on_set_cbs callback functions when set method called.
        self.__event(self.on_set.get)
        # Return self reference to allow method call chainings.
        return self

    # Decorated Method to use as an attribute to get watched/stored data
    @property
    def value(self):
        return self.__data

    # Method to append a new callback function to be ran when the set method is called
    # def on_set(self, cb):
    #     # self.__on_set_cbs.append(cb)
    #     # Return self reference to allow method call chainings.
    #     return self

    # Method to append a new callback function to be ran when the watched data is changed
    # def on_change(self, cb):
    #     self.__on_change_cbs.append(cb)
    #     # Return self reference to allow method call chainings.
    #     return self

    # def removeListener(self, cb=None):
    #     # To implement the second part where only the specified callback function is removed.
    #     # self.__cbs.clear()  # Not sure if this method works, needs to be tested
    #     # Return self reference to allow method call chainings.
    #     return self

    # "Hidden" method that is called when the data is changed, to run all the given callbacks in seperate threads
    def __event(self, callbacks):
        # Loop through and run all the callbacks as seperate threads
        for cb in callbacks:
            Thread(target=cb, daemon=True, args=(self.__data,)).start()

    """ Allow user to do w(5) to pass set method the value 5, where w = Watch(1) """
    __call__ = set


class callbacks:
    def __init__(self):
        # __on_set_cbs callback functions run the moment set method is used to set a value to the variable.
        self.__cbs = []

    def append(self, cb):
        self.__cbs.append(cb)
        return self

    def remove(self, cb):
        pass

    @property
    def get(self):
        return self.__cbs

    # __add__ = append
    # __sub__ = remove

    __iadd__ = append
    __isub__ = remove

    __call__ = append
