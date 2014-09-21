import math
from functools import lru_cache
from collections import defaultdict


@lru_cache(maxsize=None)
def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    top = int(math.floor(math.sqrt(num)))
    for i in range(3, top + 1, 2):
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

def prime_sieve(upto):
    nums = set(range(2, upto+1))
    num = 2
    while True:
        if num in nums:
            mult = 2
            while True:
                try:
                    nums.remove(mult * num)
                except KeyError:
                    pass
                if mult * num > upto:
                    break
                mult += 1
            
        elif num > upto:
            return nums

        num += 1

def phi(n):
    """
    phi(n) = n*sum_{p|n} (1 - 1/p)
    phi(n) = n*sum_{p|n} (p-1)/p
    """
    top = n
    bot = 1

    pfactors = prime_factors(n)

    for p, count in pfactors.items():
        top *= (p - 1)
        bot *= p
    return top // bot


if __name__ == '__main__':
    print(prime_sieve(1000000))
        
            
    
