import concurrent.futures
import time
from datetime import datetime

start = time.perf_counter()

def do_something(seconds):
    print(f"start time is {datetime.now()}")
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    # print('Done sleeping...')
    # yield f'Done sleeping...{seconds}'
    # return 'success'

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:           # max_workers - max to the number of processor cores.
    # with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:          # rest process will be executed after completion of previous processes
        secs = [15,14,13,12,1]
        # f1 = executor.submit(do_something,1)
        # f2 = executor.submit(do_something,1)

                # submit method schedules a function to be executed and returns a future object
                # a future object basically encapsulates the execution of our function and allows us to check on it after it's been scheduled
                # so we can check that it's running or if it's done and also check the result.
                # so if we grab the result, then it'll give us the return value of the function

        # print(f1.result())
        # print(f2.result())

                # result on the pool executor will give us the function return value
                # if we run the method, result() will wait until the function completes

        # using loop:
        # here submit add the process in order of its completion
        # results = [executor.submit(do_something, 1) for _ in range(10)]
        # results = (executor.submit(do_something, sec) for sec in secs)
        results = [executor.submit(do_something, sec) for sec in secs]
        print(results)

        for f in concurrent.futures.as_completed(results):
            print(f.result)


    finish = time.perf_counter()

    print(f'Finished in {round(finish-start,2)} second(s)')




'''
    print(processes)    When the process starts with start    # [<Process(Process-1, started)>, <Process(Process-2, started)>, ... ]
    print(processes)    When the process ends with join       # [<Process(Process-1, stopped)>, <Process(Process-2, stopped)>, ... ]
'''

# if __name__ == '__main__':
#     processes = []
#
# # Start processes in one loop
# # Arguments to methods can be passed in multiprocessing env using a list only
#     for _ in range(10):
#         p = multiprocessing.Process(target=do_something, args=[1.5])
#         p.start()
#         processes.append(p)
#
# # join each process in another loop:
#     for process in processes:
#         process.join()