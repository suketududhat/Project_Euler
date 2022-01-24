# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

prime = []

w = 0
while w < 10000:
    for i in range(3, 110000, 2):
        for n in range(2, i):
            if i % n == 0:
                break
        else:
            prime.append(i)
        w += 2

print(len(prime))
# print(prime[10000])
