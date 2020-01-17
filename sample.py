from time import sleep

from Jevents import Watch, wait_for_daemons

# Create a new data variable and store in the watchData object
sensorData = Watch(12)
# The data stored in the object can be accessed via the value property
print(sensorData.value)
# Alternatively it can also be accessed by calling itself with the help of the __repr__
print(sensorData)


# Define a callback function. All callback functions can expect a input parameter of the data watched.
def chicken(data):
    print("Chicken nuggets ", data)


# Using __iadd__ magic method to set/append an on_change callback function
sensorData.on_change += chicken

# Add a time delay to simulate real life async operations
sleep(1.4)
# Update the data in the object, this will cause all the callbacks to be called.
sensorData(1)
# Print out the updated value stored in the object.
print(sensorData)

# Add a time delay to simulate real life async operations
sleep(1.4)
# Update the data in the object. Notice nothing happens even when a new value is being set.
sensorData(5)
# Print out the updated value stored in the object.
print(sensorData)

# Call the wait function to stop main thread from ending before the daemonic threads finish
wait_for_daemons()
