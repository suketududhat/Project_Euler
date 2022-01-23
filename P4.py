# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

from itertools import product

multiple = []
palindrome = []
test = []

for x1 in range(100, 1000):
    for x2 in range(100, 1000):
        multiple.append(str(x1 * x2))

multiple.sort()

for n in multiple:
    if n == n[::-1]:
        palindrome.append(int(n))
        palindrome.sort(reverse=True)

print(max(palindrome))
# print(multiple)
