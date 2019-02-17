# Path hack to allow parent level module imports. This test script must be executed from this dir. level in the shell for hack to work
import sys, os
sys.path.insert(0, os.path.abspath('..'))
# Dependencies for the example code.
from watch import Watch
from events import wait_for_daemons
from time import sleep
import threading

# If this module is called as a standalone module to run, then execute the example code
if __name__ == "__main__":
    # Create a new data variable and store in the watchData object
    sensorData = Watch(12)
    # The data stored in the object can be accessed via the value property
    print(sensorData.value)
    # Alternatively it can also be accessed by calling itself with the help of the __repr__
    print(sensorData)

    """ Below are 4 nested function definitions that will be used as event handlers. """
    def hi(data):
        sleep(2.5)
        print('hello world ', data)

    # All callback functions can expect a input parameter of the data watched.
    def chicken(data):
        sleep(0.2)
        print('Chicken nuggets ', data)

    # The input arguemnts is a tuple, so below is another way of accessing the data.
    def on_change_cb(*data):
        print('The value has been changed ', data[0])

    def on_change_cb2(data):
        sleep(4)
        print('On change Callback function 2 ', data)

    """ Below are different ways to add above functions as event handlers """
    # Add the callbacks to the object using the on_set method
    sensorData.on_set(hi)
    # Alternative way using __add__ magic method to set/append an on_set callback function
    sensorData.on_set + chicken
    # Alternative way using __iadd__ magic method to set/append an on_change callback function
    sensorData.on_change += on_change_cb
    sensorData.on_change += on_change_cb2

    """ Change the data the first time """
    # Add a time delay to simulate real life asynchronous operations
    sleep(1.4)
    # Update the data in the object, this will cause all the callbacks to be called.
    sensorData(1)
    # Print out the updated value stored in the object.
    print(sensorData)

    """ Change the data the second time """
    # Add a time delay to simulate real life asynchronous operations
    sleep(1.4)
    # Below shows the alternative way to call the set method instead of the __call__ shorthand
    sensorData.set(2)
    # Print out the updated value stored in the object.
    print(sensorData)

    """ Set the data to the same value, so only on_set handlers are ran """
    # Add a time delay to simulate real life asynchronous operations
    sleep(1.4)
    # Update the data in the object, this will cause all the callbacks to be called.
    sensorData(2)
    # Print out the updated value stored in the object.
    print(sensorData)

    """ Below demos the removal of all the event handlers and its effects. """
    # Add a time delay to simulate real life asynchronous operations
    sleep(3)
    # Remove all the event handlers.
    # First method to remove event handlers is by removing all handlers with method call clear
    sensorData.on_set.clear()
    # Second way is to remove using the method binded to the __sub__ dunder shorthand
    sensorData.on_change - on_change_cb
    # Second way is to remove using the method binded to the __isub__ dunder shorthand
    sensorData.on_change -= on_change_cb2
    # Below is another way to remove all event handlers for on_set and on_change in one method call
    # sensorData.clearAllListeners()

    # Defining a callback function that does not take in any inputs.
    def last_cb():
        # This cb function can still run as it has been wrapped before running to prevent Errors
        print('Last cb. This does take any input arguements')

    # Add this callback to run on set method call
    sensorData.on_set += last_cb

    # Update the data in the object. Notice nothing happens even when a new value is being set.
    sensorData(5)
    # Print out the updated value stored in the object.
    print(sensorData)

    # Call the wait function to stop main thread from ending before the daemonic threads finnish
    wait_for_daemons()
