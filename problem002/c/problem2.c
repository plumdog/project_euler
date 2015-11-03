#include <stdio.h>

const int MAX = 4000000;


int fib(int n) {
        if (n <= 1) {
                return 1;
        } else {
                return fib(n - 1) + fib(n - 2);
        }
}


int sum_fibs_upto(int upto) {
        int total = 0;
        int fib_value;
        for (int i = 0; ; ++i) {
                fib_value = fib(i);
                if (fib_value > upto) {
                        break;
                }
                if (fib_value % 2 == 0) {
                        total += fib_value;
                }
        }
        return total;
}

int main() {
        printf("%d\n", sum_fibs_upto(MAX));
	return 0;
}
