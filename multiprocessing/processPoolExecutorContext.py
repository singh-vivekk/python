import concurrent.futures
import time
from datetime import datetime

start = time.perf_counter()

def do_something(seconds):
    print(f"start time is {datetime.now()}")
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    print('Done sleeping...')



if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:           # max_workers - max to the number of processor cores.
        secs = [3,2]
        # results = (executor.submit(do_something, sec) for sec in secs)
        results = [executor.map(do_something,  secs, timeout= 5)]
        # print(results)

        # for f in concurrent.futures.as_completed(results):
        for future in results:
            # retrieve the result
            print(future.result())

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start,2)} second(s)')