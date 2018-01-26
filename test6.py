import gevent
from gevent.pool import Group


def async_map(f, iterable):
    group = Group()
    return group.map(f, iterable)

def func(val):
    gevent.sleep(1)
    print(val*val)
    return val * val

async_map(func, list(range(10)))
print("NANI")