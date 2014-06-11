#include <math.h>
#include <stdio.h>

int digit(int num, int digit) {
	if(digit == 0) {
		return num % 10;
	} else {
		return (num % pow(10, digit + 1)) / digit;
	}
}

int * digit_replace(int num, int digit1, int digit2) {
	int * nums[10];

	int digit_at1 = digit(num, digit1);
	int digit_at2 = digit(num, digit2);

	num -= (digit_at1 * pow(10, digit1));
	num -= (digit_at2 * pow(10, digit2));

	int temp;

	for(int i = 0; i < 10; ++i) {
		nums[i] = num + (i * pow(10, digit1) + (i * pow(10, digit2)));
	}

	return nums;
}

int main(int argc, char *argv[]) {
	int num = 56003;
	int * replace_digits = digit_replace(num, 1, 2);

	for(int i = 0; i < 10; ++i) {
		printf("%d\n", replace_digits[i]);
	}

	return 0;
}
