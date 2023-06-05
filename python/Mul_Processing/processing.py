'''
Concurrent (Đồng thời): CPU sẽ được chia sẻ giữa các jobs để luân phiên thực hiện

Parallel (Song song): Các jobs sẽ được phân vào các CPU riêng để thực hiện.

Multithreading
    - các threads sẽ được chạy trên cùng một CPU (concurrent) chứ không
    thực hiện trên các CPU khác nhau. Do đó, khi các threads chạy các jobs
    yêu cầu nhiều tính toán thì trên thực tế, performance sẽ bị giảm chứ không
    tăng như ta thường nghĩ khi nói đến multithreading.
    - Tuy nhiên, như vậy không có nghĩa là multi-threading là vô dụng.
    Trên thực tế, multithreading có thể được sử dụng cho tác vụ IO.
    Vì với tác vụ IO, CPU không cần thực hiện gì cả mà chỉ cần đợi kết quả
    IO trả về.
    - Multithreading không phải luôn nhanh hơn serial processing.
    Thực tế, multithreading thường chỉ được sử dụng để IO.
    
Multiprocessing
    - Trong Python có hai kiểu multiprocessing thường được sử dụng đó là
    Processing và Pool.
    - Processing: Dùng để song song hóa các function. Ví dụ, ta có thể chạy
    nhiều functions trên các CPU khác nhau.
    - Pool: Dùng để song song hóa dữ liệu. Ví dụ, ta có thể chạy cùng một
    function nhưng với các bộ dữ liệu inputs khác nhau.
    - Multiprocessing luôn nhanh hơn serial processing nếu dùng đúng
    (số task <= số cores).

- There can only be one thread running at any given time in a python process.
- Multiprocessing is parallelism. Multithreading is concurrency.
- Multiprocessing is for increasing speed. Multithreading is for hiding latency.
- Multiprocessing is best for computations. Multithreading is best for IO.
- If you have CPU heavy tasks, use multiprocessing with n_process = n_cores
and never more. Never!
- If you have IO heavy tasks, use multithreading with n_threads = m * n_cores
with m a number bigger than 1 that you can tweak on your own.
Try many values and choose the one with the best speedup because there isn’t
a general rule. For instance the default value of m in ThreadPoolExecutor is
set to 5 [Source] which honestly feels quite random in my opinion.
'''

import time
import multiprocessing

def square(numbers):
    time.sleep(10)
    for x in numbers:
        print("Square: ", x*x)

def cube(numbers):
    time.sleep(10)
    for x in numbers:
        print("Cube: ", x*x*x)

if __name__ == "__main__":
    arr = [1,3,5,7,9]
    process1 = multiprocessing.Process(target=square, args=(arr,))
    process2 = multiprocessing.Process(target=cube, args=(arr,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Done process")