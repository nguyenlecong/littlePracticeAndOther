'''
Decorator
    - Decorator cho phép chúng ta nhận tham số đầu vào là một hàm khác 
    và mở rộng tính năng cho hàm đó mà không thay đổi nội dung của nó.
'''

import time

def cal_time(func):
    def timer(*args):
        start = time.time()

        result = func(*args)

        end = time.time()
        print(func.__name__, str((end-start)*1000), 'ms')

        return result

    return timer

def square(numbers):
    result = []
    start = time.time()
    for x in numbers:
        result.append(x*x)

    end = time.time()
    print('square', str((end-start)*1000) + 'ms')
    
    return result

@cal_time
def cube(numbers):
    result = []
    for x in numbers:
        result.append(x*x*x)
    
    return result

numbers = range(1,100000)

square(numbers)

cube(numbers)