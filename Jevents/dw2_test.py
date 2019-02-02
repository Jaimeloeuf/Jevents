# Dependencies for the example code.
from dw2 import Watch
from event_loop import wait_for_daemons
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

    # Below are 4 different callbacks that should run when the data changes
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

    # Add the callbacks to the object using the on_set method
    sensorData.on_set(hi)
    # Alternative way using __add__ magic method to set/append an on_set callback function
    sensorData.on_set + chicken
    # Alternative way using __iadd__ magic method to set/append an on_change callback function
    sensorData.on_change += on_change_cb
    sensorData.on_change += on_change_cb2

    # Add a time delay to simulate real life operations
    sleep(1.4)
    # Update the data in the object, this will cause all the callbacks to be called.
    sensorData(1)
    # Print out the updated value stored in the object.
    print(sensorData)

    # Add a time delay to simulate real life operations
    sleep(1.4)
    # Below shows the alternative way to call the set method instead of the __call__ shorthand
    sensorData.set(2)
    # Print out the updated value stored in the object.
    print(sensorData)

    # Add a time delay to simulate real life operations
    sleep(1.4)
    # Update the data in the object, this will cause all the callbacks to be called.
    sensorData(2)
    # Print out the updated value stored in the object.
    print(sensorData)

    # Call the wait function to stop main thread from ending before the daemonic threads finnish
    wait_for_daemons()
