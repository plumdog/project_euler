#include <stdio.h>
#include <prime.h>


int main() {
	int req = 10001;

	int value = 2;
	int prime_count = 0;

	while(1) {
		if(is_prime(value)) {
			++prime_count;
		}

		if(prime_count == req) {
			break;
		}

		++value;
	}

	printf("%d\n", value);
	return 0;
}
