#include <math.h>
#include <stdio.h>
#include <prime.h>


int ipow(int base, int exp) {
	if(exp == 0) {
		return 1;
	} else if(exp == 1) {
		return base;
	} else if(exp % 2 == 1) {
		return base * ipow(base, exp - 1);
	} else {
		int temp = ipow(base, exp / 2);
		return temp * temp;
	}
}

int add_digit_at(int num, int digit, int digit_pos) {
	int left = num / ipow(10, digit_pos);
	int right = num % ipow(10, digit_pos);

	left *= 10;
	left += digit;

	return left * ipow(10, digit_pos) + right;
}

int prime_family() {
	//int num_digits = 2;
	int trial_value1 = 0;
	int trial_value2 = 0;
	int prime_count = 0;
	int smallest_prime_in_family = 0;

	for(int num_digits = 3; num_digits < 9; ++num_digits) {
		printf("num_digits = %d\n", num_digits);
		for(int n = ipow(10, num_digits-1) + 1; n < ipow(10, num_digits); n+=2) {
			if(n % 3 == 0) {
				continue;
			}
			for(int digit1 = 0; digit1 <= num_digits; ++digit1) {
				for(int digit2 = digit1 + 1; digit2 <= num_digits + 1; ++digit2) {
					prime_count = 0;
					smallest_prime_in_family = 0;
					for(int trial_digit = 0; trial_digit < 10; ++trial_digit) {
						trial_value1 = add_digit_at(n, trial_digit, digit1);
						trial_value2 = add_digit_at(trial_value1, trial_digit, digit2);
						if(is_prime(trial_value2)) {
							if(!smallest_prime_in_family) {
								smallest_prime_in_family = trial_value2;
							}
							++prime_count;
						}
						//printf("n=%d, trial_digit=%d, digit1=%d, digit2=%d, trial_value1=%d, trial_value2=%d\n", n, trial_digit, digit1, digit2, trial_value1, trial_value2);

					}

					if(prime_count >= 7) {
						printf("prime_count == 7, smallest_prime_in_family = %d\n", smallest_prime_in_family);
					}

					if(prime_count >= 8) {
						return smallest_prime_in_family;
					}
				}
			}
		}
	}

	return 0;
}

int main(int argc, char *argv[]) {
	prime_family();
	return 0;
}
