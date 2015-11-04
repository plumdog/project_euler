#include <stdio.h>
#include <prime.h>
#include <math.h>


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
