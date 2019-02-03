#### Notes from the Watch class of data_watcher module
- Using __ double underscore to hide the attribute through attribute name mangling, to prevent user from directly modifying it.
	- print(sensorData.__on_set_cbs)  # Output: Err: no attr.
	- print(sensorData._Watch__on_set_cbs) # Output: [the callback functions, ...]
- The enumerate staticmethod returns a list of thread names of all the threads that are still alive.
	- print(threading.enumerate())
- Note that on_change callback functions are all given precedence over the on_set callback functions
- When the data is first watched with the constructor, nothing happens at all as no listeners has been attached yet.


#### Todos:
- Implement a show all listener method
- Implement a method to allow user to change the sequence in which the listeners are executed in
- Work on a 'item' watcher class and not just primitive value watcher
	- Currently the Watch class can only watch for changes/sets to primitive data types, but not objects and such as their reference stays the same. I should work on a method that will watch things like objects, through the use of hashing. By hashing the whole object and keeping a copy of it, will allow me to monitor for any change in to the object.
	- Instead of data or watch this data, change it to watch(item). So you are watching a data item and not just a data of primitive type.
- Create a v2 code to try out
	- Using a infinite loop to keep checking the variable, the moment the variable is different, run the cbs, the loop will either be threaded or subprocessed.
	- Outer loop is infinite, so to allow the user to go back to watching data with inner loop even after a temprary pause of watching.
	```py
	while True:
		while watch_flag:
			# If any change from the hidden copy, then run all the callbacks
			if _dat != data:
				self.__fire()
	```