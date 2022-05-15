from threading import Timer
import time

def func(a, b):
    print("Called function")
    return a * b

# Schedule a timer for 5 seconds
# We pass arguments 3 and 4
t = Timer(5.0, func, [3, 4])

start_time = time.time()
print(start_time)
# Start the timer
t.start()

end_time = time.time()

while end_time - start_time < 5.0:
    time.sleep(1)
    end_time = time.time()
    print("Timer will wait for sometime before calling the function")
    # print(end_time)