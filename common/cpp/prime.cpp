#include <math.h>

bool is_prime(int val) {
	int upto = static_cast<int>(sqrt(static_cast<double>(val)));

	if(val % 2 == 0) {
		return false;
	}

	for(int i = 3; i <= upto; i+=2) {
		if(val % i == 0) {
			return false;
		}
	}

	return true;
}
