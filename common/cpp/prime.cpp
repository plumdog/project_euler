#include <math.h>

bool is_prime(int val) {
	if(val == 2) {
		return true;
	}

	if(val % 2 == 0) {
		return false;
	}

	int upto = static_cast<int>(sqrt(static_cast<double>(val)));

	for(int i = 3; i <= upto+1; i+=2) {
		if(val % i == 0) {
			return false;
		}
	}

	return true;
}
