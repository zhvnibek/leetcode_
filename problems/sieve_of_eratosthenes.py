def nats(n):
    yield n
    yield from nats(n + 1)


def sieve(s=nats(2)):
    """Generator for all primes"""
    n = next(s)
    yield n
    yield from sieve(i for i in s if i % n != 0)

primes = sieve()


def first_n_primes(n=10):
    while n > 0:
        p = next(primes)
        print(p)
        n -= 1

first_n_primes()

