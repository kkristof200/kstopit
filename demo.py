import time

from kstopit import signal_timeoutable, TimeoutException

@signal_timeoutable
def f1():
    while True:
        time.sleep(0.1)

start = time.time()
res = f1(timeout=1)
duration = time.time() - start
print(type(res), res, duration)