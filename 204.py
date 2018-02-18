# Count the number of prime numbers less than a non-negative number, n.


# Simple For loop Timle limit Exceeded
def countPrimes(n):
    if n < 3:
        return 0
    elif n == 3:
        return 1
    elif n <= 5:
        return 2
    if n <= 7:
        return 3
    if n <= 10:
        return 4

    primes = [3,5,7]
    for i in range(11,n,2):
        isPrime = True
        for prime in primes:
            if i % prime == 0:
                isPrime = False
        if isPrime:
            primes.append(i)

    primes.append(2)
    return len(primes)

#Simply mark them and sum at the end. 164ms
def countPrimes2(n):
    if n<3:
        return 0
    primes = [True] * (n)
    primes[0] = False
    primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            primes[i*i:n:i]= [False] * len(primes[i*i:n:i])
    return sum(primes)
countPrimes2(10)