import multiprocessing
import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')

p1 = multiprocessing.Process(target=do_something)      # target is the place where we pass function to run
p2 = multiprocessing.Process(target=do_something)

if __name__ == '__main__':
    p1.start()              # to start the process
    p2.start()

    # join method - process will finish before moving on in scripts
    p1.join()
    p2.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start,2)} second(s)')