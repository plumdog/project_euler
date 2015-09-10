#!/usr/bin/env python3


import itertools
import fractions

def main():
    best_value = 0
    best_digits = None
    for digits in itertools.combinations(range(1, 10), 4):
        num = num_makeable_values(digits)
        if num > best_value:
            best_value = num
            best_digits = digits
    print(''.join(str(i) for i in best_digits))

        


def num_makeable_values(digits):
    if len(digits) != 4:
        raise Exception('Must give 4 digits')

    symbols = ['*', '-', '+', '/']
    digits = [fractions.Fraction(i) for i in digits]

    values_made = set()

    symbol_mixes = itertools.combinations_with_replacement(symbols, 3)
    for symbol_mix in symbol_mixes:
        full_mix = list(symbol_mix) + digits
        for rpn_list in itertools.permutations(full_mix):
            try:
                value = rpn(rpn_list)
                if value.numerator % value.denominator == 0:
                    values_made.add(value)
            except RpnError as e:
                pass

    for i in itertools.count(1):
        if i not in values_made:
            break
    return i - 1
    

class RpnError(Exception):
    pass

def rpn(list_):
    list_ = list(list_)
    value_stack = []
    while list_:
        token = list_.pop(0)
        if type(token) is fractions.Fraction:
            value_stack.append(token)
        else:
            # then its an operator
            if len(value_stack) < 2:
                raise RpnError('Insufficent values in value stack')

            v1 = value_stack.pop()
            v2 = value_stack.pop()
            if token == '*':
                value_stack.append(v1 * v2)
            elif token == '-':
                value_stack.append(v2 - v1)
            elif token == '+':
                value_stack.append(v1 + v2)
            elif token == '/':
                if v1 == 0:
                    raise RpnError('Division by zero')
                value_stack.append(v2 / v1)
            else:
                raise RpnError('Unknown operator: {}'.format(token))

    if len(value_stack) == 0:
        raise RpnError('No values in value stack')

    if len(value_stack) > 1:
        raise RpnError('Too many values in value stack: {}'.format(value_stack))

    if len(value_stack) == 1:
        return value_stack[0]


if __name__ == '__main__':
    #print(rpn([1,3,'+',4,'*',2,'/']))
    main()
