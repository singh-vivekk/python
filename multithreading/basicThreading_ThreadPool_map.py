'''
    with threading loop : for loop
'''

import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    # secs = [5,4,3,2,1]
    secs = [1,2,3,4,5]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)                                           # in order that they were started


# the map method returns the results

finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} second(s)")