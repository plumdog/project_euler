#include <stdio.h>
#include <gmp.h>
#include <string.h>


int main() {
        mpz_t exp_result;
        mpz_init(exp_result);
        mpz_ui_pow_ui(exp_result, 2, 1000);

        char* result = mpz_get_str(NULL, 10, exp_result);

        int sum = 0;
        for (int i = 0; i < strlen(result); ++i) {
                sum += result[i] - 48;
        }

	printf("%d\n", sum);
	return 0;
}
