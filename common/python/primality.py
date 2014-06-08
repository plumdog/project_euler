import math
from functools import lru_cache


@lru_cache(maxsize=None)
def is_prime(num):
    top = int(math.floor(math.sqrt(num)))
    for i in range(2, top + 1):
        if num % i == 0:
            return False
    return True
