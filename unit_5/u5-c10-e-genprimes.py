"""
Write a generator, genPrimes, that returns the sequence of prime numbers on 
successive calls to its next() method: 2, 3, 5, 7, 11, ...
"""

def genPrimes():
    x = 1
    primes = []
    while True:
        x += 1
        is_prime = True
        for p in primes:
            if x % p == 0:
                is_prime = False
                break
        if is_prime == True:
            yield x
            primes.append(x)

# test
pn = genPrimes()
print(pn.__next__())
print(pn.__next__())
print(pn.__next__())