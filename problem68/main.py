#!/usr/bin/env python3

from itertools import permutations

def range_ten_excluding(exc=()):
    return (i for i in range(1, 11) if i not in exc)
rtx = range_ten_excluding


"""
We use this slightly odd ordering as it means that we only need to
naively pick i1, i2 and i3, then we can already enforce the value for
i4. Also, we only then need to pick i5 and i6 before we can enforce
the value for i7.

       i2
         \  i8
         i9 |
        /  \|
      i3    i1
     / |    |
   i4  |    |
      i10---i6--i7
       |
      i5

"""


def reorder_result(result):
    first = result.index(min(result))
    return result[first:] + result[:first]


def concat_ordered_result(ordered_result):
    """
    [(2, 4, 10), (5, 10, 1), (8, 1, 7), (6, 7, 3), (9, 3, 4)] -> 24105101817673934
    """
    return int(''.join(''.join(str(i) for i in tup) for tup in ordered_result))


def main():
    result_strings = []

    for i1 in rtx():
        for i2 in rtx((i1,)):
            for i3 in rtx((i1, i2)):
                #    i1 + i2 + i9 == i9 + i3 + i4
                # => i1 + i2 == i3 + i4
                # => i4 = i1 + i2 - i3
                i4 = i1 + i2 - i3
                if i4 < 1:
                    # break because i3 is only getting bigger if we
                    # continue, so i4 is only getting smaller
                    break
                if (i4 > 10) or (i4 in (i1, i2, i3)):
                    continue
                for i5 in rtx((i1, i2, i3, i4)):
                    for i6 in rtx((i1, i2, i3, i4, i5)):
                        #    i3 + i10 + i5 == i10 + i6 + i7
                        # => i3 + i5 == i6 + i7
                        # => i7 = i3 + i5 - i6
                        i7 = i3 + i5 - i6
                        if i7 < 1:
                            # break because i6 is only getting bigger
                            # if we continue, so i7 is only getting
                            # smaller
                            break
                        if (i7 > 10) or (i7 in (i1, i2, i3, i4, i5, i6)):
                            continue
                        for i8 in rtx((i1, i2, i3, i4, i5, i6, i7)):
                            total = i1 + i6 + i8
                            i9 = total - i1 - i2
                            if (i9 < 1) or (i9 > 10) or (i9 in (i1, i2, i3, i4, i5, i6, i7, i8)):
                                continue
                            if i9 + i3 + i4 != total:
                                continue
                            i10 = total - i6 - i7
                            if (i10 < 1) or (i10 > 10) or (i10 in (i1, i2, i3, i4, i5, i6, i7, i8, i9)):
                                continue
                            if i3 + i10 + i5 != total:
                                continue
                            result_list = [(i2, i9, i1), (i8, i1, i6), (i7, i6, i10), (i5, i10, i3), (i4, i3, i9)]
                            result = concat_ordered_result(reorder_result(result_list))
                            if len(str(result)) == 16:
                                result_strings.append(result)

    print(max(result_strings))

if __name__ == '__main__':
    main()
