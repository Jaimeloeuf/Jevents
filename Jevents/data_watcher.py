from threading import Thread


class Watch:
    """ Watch class to implement a data-observer pattern on the encapsulated data item.
        The event-handlers/callbacks will be ran when the data is changed/set. """

    # __on_set_cbs callback functions run the moment set method is used to set a value to the variable.
    __on_set_cbs = []
    # __on_change_cbs callback functions only run if the new value set is different from the previous value.
    __on_change_cbs = []

    def __init__(self, data):
        """ Pass constructor the data item to be watched """
        self.__data = data

    # Method to set a value to the data variable watched by this class
    def set(self, data):
        # If set is called and data value has been changed, save the data and run on change callbacks
        if data != self.__data: # Check for data equality, so will not work for object references
            self.__data = data
            # Call all the __on_change_cbs callback functions
            self.__event(self.__on_change_cbs)

        # Regardless of data, call all the __on_set_cbs callback functions when set method called.
        self.__event(self.__on_set_cbs)
        # Return self reference to allow method call chainings.
        return self

    # Decorated Method to use as an attribute to get watched/stored data
    @property
    def value(self):
        return self.__data

    # Method to append a new callback function to be ran when the set method is called
    def on_set(self, cb):
        self.__on_set_cbs.append(cb)
        # Return self reference to allow method call chainings.
        return self

    # Method to append a new callback function to be ran when the watched data is changed
    def on_change(self, cb):
        self.__on_change_cbs.append(cb)
        # Return self reference to allow method call chainings.
        return self

    def removeListener(self, cb=None):
        # To implement the second part where only the specified callback function is removed.
        # self.__cbs.clear()  # Not sure if this method works, needs to be tested
        # Return self reference to allow method call chainings.
        return self

    # "Hidden" method that is called when the data is changed, to run all the given callbacks in seperate threads
    def __event(self, callbacks):
        # Loop through and run all the callbacks as seperate threads
        for cb in callbacks:
            Thread(target=cb, daemon=True, args=(self.__data,)).start()

    """ Allow user to do w(5) to pass set method the value 5, where w = Watch(1) """
    __call__ = set
    """ Allow user to do w += hello, where hello is a function passed to the on_set method """
    __iadd__ = on_set
    """ Note that there is no abbrev. for the on_change method call """