# here we will use PyTest to test the namedtuple feature in Python
from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None) # sensible defaults

def test_defaults():
    '''using no parameters should invoke the defaults'''
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2 # here is a PyTest assertion

# to run pytest we must invoke it like this:
# pytest -v using_pytest.py