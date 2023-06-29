numbers = [0, 1, 2, 3, 4]

# lambda: tạo các hàm ẩn danh, thường dùng cho các hàm sử dụng một lần và có thể viết gọn trong một dòng, 
# hữu ích trong các hàm mà hàm đó lấy kết quả một hàm khác làm đối số
square = lambda x: x*x
square(5)  # return 25

# map: áp dụng hàm đầu vào từng phần tử, thay cho vòng lặp for
list(map(square, numbers))  # return [0, 1, 4, 9, 16]

# filter: chỉ lấy ra những phần tử phù hợp bởi hàm điều kiện
list(filter(lambda x: x%2==0, numbers))  # return [0, 2, 4]

# reduce: combine mỗi 2 phần tử của arrry bằng function đầu vào,
# phép toán cộng dồn, nhân dồn, thu được một giá trị duy nhất
from functools import reduce

reduce(lambda x,y: x*y, numbers)  # return (((0*1)*2)*3)*4

reduce(lambda x,y: x*y, numbers, 5)  # return ((((5*0)*1)*2)*3)*4
