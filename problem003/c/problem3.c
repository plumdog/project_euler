#include <stdio.h>
#include <math.h>


int is_prime(long num) {
        long numsqrt = (long) sqrt((double) num);
        for (long trial = 2; trial <= numsqrt; ) {
                if (num % trial == 0) {
                        return 0;
                }

                // If the trial number if odd, then increment by
                // 2. Otherwise (ie, it is 2) increment by 1.
                if (trial % 2 == 1) {
                        trial += 2;
                } else {
                        trial += 1;
                }
        }
        return 1;
}


long largest_prime_factor(long num) {
        long numsqrt = (long) sqrt((double) num);
        long prime_factor = 0;
        for (long i = 2; i < numsqrt; ++i) {
                if ((num % i == 0) && is_prime(i)) {
                        // Don't need to check for largest, as i is
                        // always increasing.
                        prime_factor = i;
                }
        }
        return prime_factor;
}


int main() {
        long num = 600851475143;
        printf("%ld\n", largest_prime_factor(num));
	return 0;
}
