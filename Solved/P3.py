# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

number = 600851475143
prime_factors = []

for i in range(2, 10000):
    if number % i == 0:
        for x in range(2, i):
            if i % x == 0:
                break
        else:
            prime_factors.append(i)

print(prime_factors)
