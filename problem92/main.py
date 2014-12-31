#!/usr/bin/env python3


def next_in_chain(num):
    total = 0
    while num != 0:
        digit = num % 10
        num = num // 10
        total += digit * digit
    return total


def main(upto):
    ends_at_89 = set()
    ends_at_1 = set()

    for i in range(1, upto):
        trial = i
        while True:
            if (trial == 1) or (trial in ends_at_1):
                ends_at_1.add(i)
                break

            if (trial == 89) or (trial in ends_at_89):
                ends_at_89.add(i)
                break

            trial = next_in_chain(trial)
    print(len(ends_at_89))
            
            

if __name__ == '__main__':
    #main(1000000)
    main(10000000)
