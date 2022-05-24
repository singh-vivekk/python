'''
The Process class
In multiprocessing, processes are spawned by creating a Process object and then calling its start() method.
Process follows the API of threading.Thread.
'''
'''
from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
'''
# To show the individual process IDs involved, here is an expanded example:
from multiprocessing import Process
import multiprocessing as mp
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print("No. of processors: ",mp.cpu_count())
    print(" current_process() : ", mp.current_process())
    print(" get_start_method(allow_none=False) : ", mp.get_start_method(allow_none=False))
    # print(" parent_process() : ", mp.parent_process())
    print(" get_all_start_methods() : ", mp.get_all_start_methods())          #  On Windows only 'spawn' is available. On Unix 'fork' and 'spawn' are always supported, with 'fork' being the default.

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()