Using __ double underscore to hide the attribute through attribute name mangling, to prevent user from directly modifying it.
print(sensorData.__cbs)  # Output: Err: no attr.
print(sensorData._Watch__cbs) # Output: [the callback functions, ...]

The enumerate staticmethod returns a list of thread names of all the threads that are still alive.
print(threading.enumerate())


The first time u "set" a value, or should I say, watch the value, nothing happens at all, as no listeners has been attached yet.

Maybe I can have 2 types of callbacks!
a proprety created by decoroators and

one called on_set and one called on_change

then u can do something like,
data.on_set += cb
data.on_change += cb

Another version of watch class can be using a infinite loop to keep checking
the variable, the moment the variable is different, run the cbs, the loop will
either be threaded or subprocessed.


# Outer loop is infinite, so to allow the user to go back to watching data with inner loop even after a temprary pause of watching.
while True:
	while watch_flag:
		# If any change from the hidden copy, then run all the callbacks
		if _dat != data:
			self.__fire()



Also pas the data value into the callbacks. All cbs should expect such a value.


Instead of data, which like watch this data, change it to watch(item). So you 
are watching a data item and not just a data of primitive type.

Names:
	Watch
	Track
	Observe


This class should be part of the events package,
so like you do a, from events import Track
data = Track(dat)

data.set(8)









@Todos
- Implement a show all listener method
- Implement a remove listener method
	- By probably using a ID that is associated with the enumeration of the callback(s) array
- Implement a method to allow user to change the sequence in which the listeners are executed in
- Currently the Watch class can only watch for changes/sets to primitive data types, but not
	objects and such as their reference stays the same. I should work on a method that will watch
	things like objects, through the use of hashing. By hashing the whole object and keeping a copy
	of it, will allow me to monitor for any change in to the object.


Note that on_change callback functions are all given precedence over the on_set callback functions