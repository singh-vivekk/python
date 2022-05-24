'''
The multiprocessing module also introduces APIs which do not have analogs in the threading module.
A prime example of this is the Pool object which offers a convenient means of parallelizing the execution of a function across multiple input values, distributing the input data across processes (data parallelism).
The following example demonstrates the common practice of defining such functions in a module so that child processes can successfully import that module.
This basic example of data parallelism using Pool
'''
# The Pool class:
from multiprocessing import Pool

def f(x):
    return x*x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

# output: [1, 8, 27]

