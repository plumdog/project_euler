#include <stdio.h>


int sum_multiples_of_three_and_five(int upto) {
        int total = 0;
        for (int i = 1; i < upto; ++i) {
                if ((i % 3 == 0) || (i % 5 == 0)) {
                        total += i;
                }
        }
        return total;
}

int main() {
        printf("%d\n", sum_multiples_of_three_and_five(1000));
	return 0;
}
