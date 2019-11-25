def e():
    prime_to_find = 10001
    x = 3
    primes = [2]
    while len(primes) < prime_to_find:
        if all(x % prime for prime in primes):
            primes.append(x)
        else:
            x += 1
    return primes[-1]


print(e())
