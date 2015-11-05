#include <stdio.h>
#include <math.h>


int num_divisors(int num) {
        if (num < 1)
                return -1;

        if (num == 1)
                return 1;

        int count = 2; // We always have 2, namely: 1 and num
        int sqroot = (int) sqrt((double) num);

        for (int i = 2; i <= sqroot; ++i) {
                if (num % i == 0)
                        count += 2;
        }

        if (sqroot * sqroot == num) {
                // If the number is a square, we'll have counted the
                // sqrt twice.
                count--;
        }
        return count;
}


int triangle(int num) {
        return num * (num + 1) / 2;
}


int first_traingle_with_divisors(int num_divs) {
        int tri;
        int divs;
        for (int i = 1; ; ++i) {
                tri = triangle(i);
                divs = num_divisors(tri);
                if (divs > num_divs) {
                        return tri;
                }
        }
}


int main() {
        printf("%d\n", first_traingle_with_divisors(500));
}
