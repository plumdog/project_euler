#include <math.h>

int is_prime(int val) {
	if(val == 2) {
		return 1;
	}

	if(val % 2 == 0) {
		return 0;
	}

	int upto = (int) sqrt((double) val);

	for(int i = 3; i <= upto+1; i+=2) {
		if(val % i == 0) {
			return 0;
		}
	}

	return 1;
}
