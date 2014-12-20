#!/usr/bin/env python3

import sys

def main():
    with open(sys.argv[1]) as f:
        nums = f.read().splitlines()
    total_length = 0
    total_length_shortened = 0
    for num in nums:
        total_length += len(num)
        total_length_shortened += min_length(num)
    print(total_length - total_length_shortened)
    

def min_length(numeral):
    as_int = to_int(numeral)
    as_numeral = to_numeral(as_int)
    return len(as_numeral)


def symbol_to_int(symbol):
    symbols = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    return symbols[symbol]


def int_to_symbol(int_):
    ints = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'}
    return ints[int_]


def parse_numeral(numeral):
    in_segs = []
    current_symbol = None
    current_count = 0

    for symbol in numeral:
        if (current_symbol is not None) and (current_symbol != symbol):
            in_segs.append((current_symbol, current_count))
            current_symbol = symbol
            current_count = 1
        else:
            current_count += 1

        if current_symbol is None:
            current_symbol = symbol

    if current_count:
        in_segs.append((current_symbol, current_count))
    return in_segs


def to_int(numeral):
    values = []
    last_symbol = None
    for symbol, count in parse_numeral(numeral):
        if last_symbol and (symbol_to_int(last_symbol) < symbol_to_int(symbol)):
            values[-1] = -values[-1]
        values.append(symbol_to_int(symbol) * count)
        last_symbol = symbol
    return sum(values)


def int_powers_and_digits(int_):
    return reversed(list(enumerate(reversed([int(i) for i in str(int_)]))))


def to_numeral(int_):
    numeral = []
    for power, digit in int_powers_and_digits(int_):
        numeral.append(digit_to_numeral(power, digit))
    return ''.join(numeral)


def digit_to_numeral(power, digit):
    if power == 0:
        return _digit_to_numeral(digit, 1, 5, 10)
    elif power == 1:
        return _digit_to_numeral(digit, 10, 50, 100)
    elif power == 2:
        return _digit_to_numeral(digit, 100, 500, 1000)
    elif power == 3:
        return int_to_symbol(1000)*digit
    else:
        raise Exception('Too big!')


def _digit_to_numeral(digit, unit, five, ten):
    if digit == 0:
        return ''
    elif digit <= 3:
        return int_to_symbol(unit)*digit
    elif digit == 4:
        return int_to_symbol(unit) + int_to_symbol(five)
    elif digit <= 8:
        return int_to_symbol(five) + int_to_symbol(unit)*(digit-(five // unit))
    elif digit == 9:
        return int_to_symbol(unit) + int_to_symbol(ten)
    else:
        raise Exception('Invalid digit: {}'.format(digit))
    


if __name__ == '__main__':
    main()
