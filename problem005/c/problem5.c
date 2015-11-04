#include <stdio.h>
#include <math.h>
#include <prime.h>


int step_size(int by_all_upto) {
        int step = 1;
        for (int i = 2; i <= by_all_upto; ++i) {
                if (is_prime(i)) {
                        step *= i;
                }
        }
        return step;
}


int divisible_by_all_upto(int val, int upto) {
        int all = 1;
        for (int i = 2; i <= upto; ++i) {
                if(val % i != 0) {
                        return 0;
                }
        }
        return 1;
}


int smallest_divisible(int by_all_upto) {
        int step = step_size(by_all_upto);
        for(int n = step; ; n+=step) {
                if (divisible_by_all_upto(n, by_all_upto)) {
                        return n;
                }
        }
}


int main() {
        printf("%d\n", smallest_divisible(20));
	return 0;
}
