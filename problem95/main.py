#!/usr/bin/env python3


#import sys
#sys.path.insert(0, '../common/python/')

#import primality
import sys
import collections
import itertools

#sys.setrecursionlimit(40)


def get_chain(factor_sum, root, k=None, chain=None):
    if k is None:
        k = root
    if chain is None:
        chain = []

    next_ = factor_sum[k]

    if next_ == 1:
        raise ValueError
    if next_ in chain:
        return (chain, next_)
    if next_ == k:
        raise ValueError

    chain.append(next_)
    return get_chain(factor_sum, root, next_, chain)


def main():
    #max_ = 1000000
    max_ = 1000000

    factor_sum = collections.defaultdict(int)
    for i in range(1, max_ // 2):
        

        for j in itertools.count(2):
            if i * j > max_:
                break
            factor_sum[i * j] += i

    

    factor_sum = dict(factor_sum)

    #print(get_chain(factor_sum, 284, 284))
    #return
                    

    loops = {}
    for k in factor_sum.keys():
        #print('##############', k)
        try:
            chain, loopback = get_chain(factor_sum, k, k)
            if chain and (loopback == chain[0]):
                loops[k] = (chain, loopback)
        except (KeyError, ValueError):
            pass

    longest_chain_length = 0
    longest_chain = None
    for start, (chain, _) in loops.items():
        len_ = len(chain)
        if len_ > longest_chain_length:
            longest_chain_length = len_
            longest_chain = chain
    print(min(longest_chain))
            

if __name__ == '__main__':
    #import cProfile
    #cProfile.run('main()')
    main()
