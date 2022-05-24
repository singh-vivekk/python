import multiprocessing
import time

start = time.perf_counter()

def do_something(x):
    print('Sleeping 1 second...')
    time.sleep(1)
    print(x)
    print('Done sleeping...')

if __name__ == '__main__':
    processes = []

# Start processes in one loop
    for j in range(10):
        for i in [1,2]:
            p = multiprocessing.Process(target=do_something, args=[i])
            p.start()
            processes.append(p)

# join each process in another loop:
    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start,2)} second(s)')


'''
    print(processes)    When the process starts with start    # [<Process(Process-1, started)>, <Process(Process-2, started)>, ... ]
    print(processes)    When the process ends with join       # [<Process(Process-1, stopped)>, <Process(Process-2, stopped)>, ... ]
'''