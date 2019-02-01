# Dependencies for the example code.
from data_watcher import Watch
from event_loop import wait_for_daemons
from time import sleep
import threading

# If this module is called as a standalone module to run, then execute the example code
if __name__ == "__main__":
    # Create a new data variable and store in the watchData object
    sensorData = Watch(12)
    # The data stored in the object can only be accessed via the value property
    print(sensorData.value)

    # Below are 3 different callbacks that should run when the data changes
    def hi():
        sleep(2.5)
        print('hello world')

    def chicken():
        sleep(0.2)
        print('Chicken nuggets')

    def on_change_cb():
        print('The value has been changed')

    # Add the callbacks to the object
    sensorData.on_set(hi)
    sensorData.on_set(chicken)
    sensorData.on_change(on_change_cb)

    # Add a time delay to simulate real life operations
    sleep(1.4)
    # Update the data in the object, this will cause all the callbacks to be called.
    sensorData.set(1)
    # Print out the updated value stored in the object.
    print(sensorData.value)

    # Add a time delay to simulate real life operations
    sleep(1.4)
    # Update the data in the object, this will cause all the callbacks to be called.
    sensorData.set(2)
    # Print out the updated value stored in the object.
    print(sensorData.value)

    # Add a time delay to simulate real life operations
    sleep(1.4)
    # Update the data in the object, this will cause all the callbacks to be called.
    sensorData.set(2)
    # Print out the updated value stored in the object.
    print(sensorData.value)

    # Call the wait function to stop main thread from ending before the daemonic threads finnish
    wait_for_daemons()
