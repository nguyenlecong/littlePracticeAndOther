import time
import threading

def square(numbers):
    for x in numbers:
        time.sleep(1)
        print("Square: ", x*x)

def cube(numbers):
    for x in numbers:
        time.sleep(1)
        print("Cube: ", x*x*x)

t = time.time()
arr = [1,3,5,7,9]

# Not use multi-thread -> 10 seconds
# square(arr)
# cube(arr)

# Use multi-thread -> 5 seconds
thread1 = threading.Thread(target=square, args=(arr,))
thread2 = threading.Thread(target=cube, args=(arr,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Done in: ", time.time() - t)