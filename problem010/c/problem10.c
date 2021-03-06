#include <stdio.h>
#include <prime.h>


int main() {
	int top = 2000000;
	int trial;

	long long total = 2; // include 2

	for(int trial = 3; trial < top; ++trial) {
		if(is_prime(trial)) {
			total += trial;
		}
	}

	printf("%lld\n", total);
}
