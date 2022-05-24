'''
    with threading
'''

import threading
import time

start = time.perf_counter()

def do_something():
    print('sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

t1 = threading.Thread(target=do_something)     # necessarily not a function call like do_something()
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()     # To ensure that the thread completes before moving next line

finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} second(s)")