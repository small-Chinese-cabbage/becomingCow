# generate an odd number list
def _odd_iter_():
    n = 1
    while True:
        n = n + 2
        yield n


# return a number list in which the numbers cannot be divided evenly by n
def _not_divisible_(n):
    return lambda x: x % n > 0


# define a generator, return the next prime continiously
def primes():
    yield 2
    it = _odd_iter_()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible_(n), it)


for n in primes():
    if n < 1000:
        print(n)
    else:
        break
