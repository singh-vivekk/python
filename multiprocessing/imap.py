# imap() or any mapping function takes one value and 'maps' it to another via the function's return value. In the snippet you posted, function() doesn't return anything.

import multiprocessing

def function(a):
    v = a**2
    w = a**3
    x = a**4
    y = a**5
    z = a**6
    return v, w, x, y, z

b = [1,2,3,4,5,6,7,8,9,10]

vals = []

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    vals = pool.imap(function, b, 2)


for i in vals:
    print(i)


'''
On Windows the subprocesses will import (i.e. execute) the main module at start. You need to insert an if __name__ == '__main__': guard in the main module to avoid creating subprocesses recursively.

Modified testMain.py:

import parallelTestModule

if __name__ == '__main__':    
    extractor = parallelTestModule.ParallelExtractor()
    extractor.runInParallel(numProcesses=2, numThreads=4)
'''