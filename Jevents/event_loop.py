import threading

# Blocking function that waits for all the daemon threads to end by calling join method on them.
def wait_for_daemons():
	# Wait for all daemonic threads to end before ending the main thread, which will kill any still-alive daemonic threads.
	for thread in threading.enumerate():
		if thread.daemon:
			thread.join()
