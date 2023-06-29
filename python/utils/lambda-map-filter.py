numbers = [0, 1, 2, 3, 4]

# lambda
square = lambda x: x*x
square(5)  # return 25

# map
list(map(square, numbers))  # return [0, 1, 4, 9, 16]

# filter
list(filter(lambda x: x%2==0, numbers))  # return [0, 2, 4]
