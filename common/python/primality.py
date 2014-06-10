import math
from functools import lru_cache
from collections import defaultdict


@lru_cache(maxsize=None)
def is_prime(num):
    top = int(math.floor(math.sqrt(num)))
    for i in range(2, top + 1):
        if num % i == 0:
            return False
    return True


def prime_factors(num):
    if num <= 1:
        return defaultdict(int)

    prime_divs = defaultdict(int)

    trial = 2
    num_ = num
    top = int(math.sqrt(num_))

    while True:
        if trial > top:
            d = defaultdict(int)
            d[num_] = 1
            return d

        if num_ % trial == 0:
            parent = prime_factors(num_ // trial)
            parent[trial] += 1
            return parent
        else:
            if trial == 2:
                trial += 1
            else:
                trial += 2
