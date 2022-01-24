# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
# 3025 - 385 = 2640
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


# def sum_of_squares(n1, n2, s=0):
#     for i in range(n1, n2):
#         s += i ** 2
#     return s
#
#
# def square_of_sum(n1, n2, s=0):
#     for i in range(n1, n2):
#         s += i
#     return s ** 2


def difference(n1, n2):
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(n1, n2):
        sum_of_squares += i ** 2
        square_of_sum += i
    print((square_of_sum**2) - sum_of_squares)


difference(1, 101)
