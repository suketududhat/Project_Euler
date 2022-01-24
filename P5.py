# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

n = 2520

multiples = []

for i in range(1,11):
    if n % i == 0:
        multiples.append(i)

print(multiples)