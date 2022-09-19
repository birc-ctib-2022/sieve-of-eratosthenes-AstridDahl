"""Computing primes."""

n=50

def sieve(n: int) -> list[int]:
    """
    Compute all the primes up to (and possibly including) `n`.

    `n` must be positive.

    >>> sieve(15)
    [2, 3, 5, 7, 11, 13]

    """
    assert n > 0
    candidates = list(range(2, n + 1))
    primes = []

    while candidates:
        p=candidates[0]
        candidates = [cand for cand in candidates if cand % p != 0]

        primes.append(p)  

    # FIXME: fill out this bit

    return primes

print(sieve(15))