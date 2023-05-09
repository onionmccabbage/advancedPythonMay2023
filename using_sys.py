import sys # this is a reference to the system upon which Python is running
print(sys.version) # version of Python
print(sys.path) # all the places Python will look for imports
print(sys.platform) # what platform (Win, Mac, Linux etc,)
print(sys.base_prefix) # a very precise indication of which version of Python

# there are a handful of 'flavours' of Python
# cpython (the most common, written in c)
# ipython (optimized for interactivity - used in Jupyter)
# jython  (written in Java)
# ironpython (written in .net)