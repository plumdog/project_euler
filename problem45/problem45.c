#include <math.h>
#include <stdio.h>

long long hexagonal(long n) {
	return n * (2*n - 1);
}

int is_pentagonal(long long number) {
	long long temp = 1 + 24*number;
	long long sq = (long long) sqrt(temp);
	return (sq*sq == temp) && (sq % 6 == 5);
}

int is_triangular(long long number) {
	long long temp = 1+8*number;
	long long sq = (long long) sqrt(1+8*number);
	return (temp == sq*sq) && (sq % 2 == 1);
}

int main(int argc, char *argv[]) {
	long long trial = 0;

	// Start at 144, as we want the result that comes after the 143
	// hexagonal number.
	for(long n = 144; ; ++n) {
		trial = hexagonal(n);
		if(is_pentagonal(trial) && is_triangular(trial)) {
			printf("%lld\n", trial);
			return 0;
		}
	}

	return 0;
}
