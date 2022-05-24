import multiprocessing
import time
import os
start = time.perf_counter()
from datetime import datetime

''' 
    In order to pass arguments to a multi-processing process, the arguments must be able to be serialized using pickle 
    pickle means - serializing something with pickle means that we are converting Python objects into a format that can be 
    deconstructed and reconstructed in another python script
'''


def do_something(seconds):
    # print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    # print('Done sleeping...')

if __name__ == '__main__':
    processes = []

# Start processes in one loop
# Arguments to methods can be passed in multiprocessing env using a list only
    for i in range(8):
        # time.sleep(1)
        k = 8
        if i == 5:
            k = 20

        p = multiprocessing.Process(target=do_something, args=[k])
        print(f"{p} started at {datetime.now()}")
        p.start()
        processes.append(p)

# join each process in another loop:
    for process in processes:
        print(f"wait for {process} called at {datetime.now()}")
        process.join(5)
        print(f"wait for {process} ended at {datetime.now()}")

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start,2)} second(s)')

    print("existing")
    os._exit(0)
    print("exited")

'''
    print(processes)    When the process starts with start    # [<Process(Process-1, started)>, <Process(Process-2, started)>, ... ]
    print(processes)    When the process ends with join       # [<Process(Process-1, stopped)>, <Process(Process-2, stopped)>, ... ]
'''