'''
Generator
    - tiet kiem thoi gian hon list
    - tiet kiem bo nho hon list
    - khi khong can luu gia tri, chi can tao ra du lieu
'''
def square_nums(list_nums):
    for x in list_nums:
        yield x*x
    
list_nums = [1,2,3]

# generated = square_nums(list_nums)

# print(generated)
# print(list(generated))

# print(next(generated))
# print(next(generated))
# print(next(generated))
# # print(next(generated))

new_generator = (x*x for x in list_nums)

# print(new_generator)
# print(list(new_generator))

print(next(new_generator))
print(next(new_generator))
print(next(new_generator))
# print(next(new_generator))
