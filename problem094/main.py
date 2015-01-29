#!/usr/bin/env python3


def main(max_):
    total_perim = 0
    x = 2
    y = 1

    while True:
        # b = a + 1
        three_a = 2 * x + 1
        h = y

        if three_a % 3 == 0:
            a = three_a // 3

            perim = 2 * a + (a + 1) # a + a + b
            two_area = (a + 1) * h
            if two_area % 2 == 0:
                area = two_area // 2
                if (perim <= max_) and area:
                    total_perim += perim

        # b = a - 1
        three_a = 2 * x - 1
        h = y

        if three_a % 3 == 0:
            a = three_a // 3

            perim = 2 * a + (a - 1) # a + a + b

            # this is the smaller of the two perimeters that we
            # calculate, so if this one is too big, then give up
            # seaching.
            if perim > max_:
                break

            two_area = (a - 1) * h
            if two_area % 2 == 0:
                area = two_area // 2
                if (perim <= max_) and area:
                    total_perim += perim

        x, y = (2 * x + 3 * y,
                2 * y + x)
        
    return total_perim
    

if __name__ == '__main__':
    print(main(1000000000))
