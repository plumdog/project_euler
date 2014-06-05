#include <math.h>

bool is_prime(int val) {
	int upto = static_cast<int>(sqrt(static_cast<double>(val)));

	for(int i = 2; i <= upto; ++i) {
		if(val % i == 0) {
			return false;
		}
	}

	return true;
}
