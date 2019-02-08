from threading import Thread


class Watch:
    """ Watch class to implement a data-observer pattern on the encapsulated data item.
        The event-handlers/callbacks will be ran when the data is changed/set. """

    def __init__(self, data=None):
        """ Pass constructor the data item to be watched. None by default """
        self.__data = data
        # Create 2 Callback objects to store all the callback functions
        self.on_set = Callback()
        self.on_change = Callback()

    # Decorated Method to use as an attribute to get watched/stored data
    @property
    def value(self):
        return self.__data

    # Method to set a value to the data variable watched by this class
    def set(self, data, *args, **kwargs):
        # If set is called and data value has been changed, save the data and run on change callbacks
        if data != self.__data:  # Check for data equality, so will not work for object references
            self.__data = data
            # Run all the on_change callback functions
            self.on_change.run(self.__data, args, kwargs)

        # Always run all the on_set callback functions when set method is called
        self.on_set.run(self.__data, args, kwargs)
        # Return self reference to allow method call chainings.
        return self
    
	# Method to remove all the Callbacks associated with the data
    def clearAllListeners(self):
        self.on_set.clear()
        self.on_change.clear()
    
    # Method to return the string representation when str(obj) called
    def __str__(self):
        # 2 different ways to get the string representation.
        # Method 1 better for objects for their string representation
        return str(self.__data)
        # Method 2 better for primitive data types
        # return '{}'.format(self.__data)

    # Allow user to call w to get data instead of w.value, where w = Watch(1)
    __repr__ = value
    # Allow user to do w(5) to pass set method the value 5, where w = Watch(1)
    __call__ = set


class Callback:
    """
        For the 'append' and 'remove' methods
        Return self is NEEDED to allow user to call "data.on_set_callbacks += new_cb"
        This is because if nothing is returned, the on_set_callbacks property of the data object
        will be overwritten to point to new_cb instead of the callbacks with new_cb inside.
    """

    def __init__(self, cbs=None):
        """ Able to accept pre-constructed lists of callback functions """
        if cbs == None:
            # Create an empty list for this Callback object if none given
            self.__cbs = []
        else:
            self.__cbs = cbs

    # Method to get the callback-function list out from the object
    @property
    def get(self):
        return self.__cbs

    # Static Decorator function that wraps original function in try/except block
    @staticmethod
    def fn_wrapper(fn):
        """ Callbacks are not wrapped on saving them into Callback Class objects because
            when wrapped, their reference changes, and thus making it unable to be removed
            from the list of callbacks using the reference to the original function.
            Thus the wrapper should only be applied just before running the functions.
        """
        # Define the inner wrapper function
        def wrapped_fn(*args, **kwargs):
            try:
                # Try to call the original callback function with the arguements
                fn(*args, **kwargs)
            except TypeError:
                # If the function does not except the arguements, call without any
                fn()
                # Below is alternative fn call with kwargs
                # fn(**kwargs)
            except:
                # If the exception raised is not a TypeError, log it out
                print('ERR: Unknown exception raised when calling callback function')
        
        # Return the wrapped function back
        return wrapped_fn


    def run(self, data, *args, **kwargs):
        # Loop through and run all the callbacks in seperate threads
        for cb in self.__cbs:
            # The thread is used to run the wrapped function
            Thread(target=self.fn_wrapper(cb), daemon=True, args=(data,), kwargs=kwargs).start()

        # Return self reference to allow method call chainings.
        return self

    # Method to append data/callback-functions into the list
    def append(self, cb):
        self.__cbs.append(cb)
        # Return self reference to allow method call chainings.
        return self

    # Method to remove data/callback-functions from the list
    def remove(self, cb):
        try:
            self.__cbs.remove(cb)
        except ValueError:
            print('Invalid callback reference received for removing from "Callback" object!')
            raise # Re-raise the Exception to print stack traceback and stop program execution
        # Return self reference to allow method call chainings.
        return self

    # Method to clear all callback-functions from the list
    def clear(self):
        self.__cbs.clear()
        # Return self reference to allow method call chainings.
        return self

    # Magic method to allow use of len() function call on this Class of objects
    def __len__(self):
        return len(self.__cbs)

    # Shorthand to allow user to get the iterable by calling Callback_list instead of Callback_list.value
    def __iter__(self):
        # By using the iterable form from the list itself, __next__ does not need to be implemented
        return iter(self.__cbs)

    # Allow user to use these dunder methods to do +, -, +=, -= operations on this class of objects
    __add__ = __iadd__ = append
    __sub__ = __isub__ = remove
    # Shorthand to allow user to append callback by calling callback(value)
    __call__ = append
    # Allow user to get the list when called directly, by using the get method
    __repr__ = get
    
    # Working on making this into a 'dict' like object to call callbacks specifically.
    # def __getitem__(self, )
