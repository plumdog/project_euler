#include <iostream>
#include <math.h>

using namespace std;

bool is_prime(int val) {
	int upto = static_cast<int>(sqrt(static_cast<double>(val)));

	for(int i = 2; i <= upto; ++i) {
		if(val % i == 0) {
			return false;
		}
	}

	return true;
}

int main() {
	int req = 10001;

	int value = 2;
	int prime_count = 0;

	while(true) {
		if(is_prime(value)) {
			++prime_count;
		}

		if(prime_count == req) {
			break;
		}

		++value;
    }

	cout << value << endl;
  	return 0;
}

